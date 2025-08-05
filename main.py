from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator
from typing import Optional, List
import httpx
import base64
import json
import os
from phone_validator import PhoneValidator

app = FastAPI(
    title="API de Validação de Celular",
    description="API para validar números de celular brasileiros e identificar operadoras",
    version="1.0.0"
)

# Configurar CORS para permitir acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instância global do validador
phone_validator = PhoneValidator()

# Configuração da API Gemini
GEMINI_API_KEY = "AIzaSyBu2oagQERfHTyrWLfvWJ1r-434jGS_4ts"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"

class PhoneNumberRequest(BaseModel):
    phone_number: str
    
    @validator('phone_number')
    def validate_phone_format(cls, v):
        # Remove todos os caracteres não numéricos
        digits_only = ''.join(filter(str.isdigit, v))
        
        if len(digits_only) < 11 or len(digits_only) > 13:
            raise ValueError('O número deve ter entre 11 e 13 dígitos')
        
        return v

class PhoneNumberResponse(BaseModel):
    original_number: str
    formatted_number: Optional[str] = None
    is_valid: bool
    country_code: Optional[str] = None
    area_code: Optional[str] = None
    number: Optional[str] = None
    operator: Optional[str] = None
    operator_info: Optional[dict] = None
    error_message: Optional[str] = None

class ChatMessage(BaseModel):
    message: str
    is_audio: bool = False
    audio_data: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    success: bool
    error_message: Optional[str] = None

class AudioTranscriptionRequest(BaseModel):
    audio_data: str  # Base64 encoded audio data

class AudioTranscriptionResponse(BaseModel):
    text: str
    success: bool
    error_message: Optional[str] = None

@app.get("/")
async def root():
    return {
        "message": "API de Validação de Celular Brasileiro",
        "version": "1.0.0",
        "endpoints": {
            "/validate": "POST - Validar número de celular",
            "/docs": "Documentação da API",
            "/health": "Verificar status da API"
        },
        "features": [
            "Validação de números de celular brasileiros",
            "Formatação automática no padrão 55 11 98877 6655",
            "Adição automática do código do país (55)",
            "Validação de DDD e formato",
            "Consulta de operadora via múltiplas fontes",
            "APIs externas (NumVerify, Abstract) - 100 consultas gratuitas/mês",
            "ABR Telecom (Site Oficial) como fonte alternativa",
            "Mapeamento local como fallback"
        ]
    }

@app.post("/validate", response_model=PhoneNumberResponse)
async def validate_phone_number(request: PhoneNumberRequest):
    try:
        # Usa o validador para processar o número
        result = phone_validator.validate_phone(request.phone_number)
        
        if not result["is_valid"]:
            return PhoneNumberResponse(
                original_number=result["original_number"],
                is_valid=False,
                error_message=result["error_message"]
            )
        
        return PhoneNumberResponse(
            original_number=result["original_number"],
            formatted_number=result["formatted_number"],
            is_valid=True,
            country_code=result["country_code"],
            area_code=result["area_code"],
            number=result["number"],
            operator=result["operator"],
            operator_info=result["operator_info"]
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@app.get("/validate/{phone_number}")
async def validate_phone_number_get(phone_number: str):
    """Endpoint GET para validação rápida via URL"""
    try:
        result = phone_validator.validate_phone(phone_number)
        
        if not result["is_valid"]:
            return {
                "is_valid": False,
                "error": result["error_message"],
                "original_number": phone_number
            }
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy", 
        "service": "phone-validation-api",
        "version": "1.0.0",
        "features": {
            "brazilian_phone_validation": True,
            "auto_formatting": True,
            "operator_detection": True
        }
    }

@app.get("/examples")
async def get_examples():
    """Retorna exemplos de números para teste"""
    return {
        "valid_examples": [
            "11988776655",
            "5511988776655",
            "11 98877 6655",
            "(11) 98877-6655",
            "+55 11 98877 6655"
        ],
        "invalid_examples": [
            "1234567890",  # Muito curto
            "123456789012345",  # Muito longo
            "11987654321",  # Não começa com 9
            "5511987654321"  # Não começa com 9
        ],
        "expected_format": "55 11 98877 6655"
    }

async def call_gemini_api(prompt: str) -> str:
    """Chama a API do Gemini para gerar resposta"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
                json={
                    "contents": [
                        {
                            "parts": [
                                {
                                    "text": f"""Você é um assistente especializado em validação de números de celular brasileiros. 
                                    Responda de forma clara e concisa em português brasileiro.
                                    
                                    Pergunta do usuário: {prompt}
                                    
                                    Se a pergunta for sobre validação de números de celular, explique sobre:
                                    - Formato esperado: 55 11 98877 6655
                                    - DDDs válidos no Brasil
                                    - Operadoras (Vivo, Claro, TIM, etc.)
                                    - Como usar a API de validação
                                    
                                    Se for uma pergunta geral, responda de forma útil e amigável."""
                                }
                            ]
                        }
                    ]
                },
                timeout=30.0
            )
            
            if response.status_code == 200:
                data = response.json()
                if "candidates" in data and len(data["candidates"]) > 0:
                    return data["candidates"][0]["content"]["parts"][0]["text"]
                else:
                    return "Desculpe, não consegui processar sua pergunta. Tente novamente."
            else:
                return f"Erro na API do Gemini: {response.status_code}"
                
    except Exception as e:
        return f"Erro ao conectar com a API do Gemini: {str(e)}"

@app.post("/chat", response_model=ChatResponse)
async def chat_with_bot(request: ChatMessage):
    """Endpoint para chat com o bot usando Gemini"""
    try:
        message = request.message.strip()
        
        if not message:
            return ChatResponse(
                response="Por favor, digite uma mensagem.",
                success=False,
                error_message="Mensagem vazia"
            )
        
        # Chama a API do Gemini
        response = await call_gemini_api(message)
        
        return ChatResponse(
            response=response,
            success=True
        )
        
    except Exception as e:
        return ChatResponse(
            response="Desculpe, ocorreu um erro ao processar sua mensagem.",
            success=False,
            error_message=str(e)
        )

@app.post("/transcribe-audio", response_model=AudioTranscriptionResponse)
async def transcribe_audio(request: AudioTranscriptionRequest):
    """Endpoint para transcrever áudio usando Gemini"""
    try:
        # Decodifica o áudio base64
        audio_data = base64.b64decode(request.audio_data)
        
        # Chama a API do Gemini para transcrição
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}",
                json={
                    "contents": [
                        {
                            "parts": [
                                {
                                    "text": "Transcreva o seguinte áudio para texto em português brasileiro:"
                                },
                                {
                                    "inline_data": {
                                        "mime_type": "audio/wav",
                                        "data": request.audio_data
                                    }
                                }
                            ]
                        }
                    ]
                },
                timeout=30.0
            )
            
            if response.status_code == 200:
                data = response.json()
                if "candidates" in data and len(data["candidates"]) > 0:
                    transcribed_text = data["candidates"][0]["content"]["parts"][0]["text"]
                    return AudioTranscriptionResponse(
                        text=transcribed_text,
                        success=True
                    )
                else:
                    return AudioTranscriptionResponse(
                        text="",
                        success=False,
                        error_message="Não foi possível transcrever o áudio"
                    )
            else:
                return AudioTranscriptionResponse(
                    text="",
                    success=False,
                    error_message=f"Erro na API: {response.status_code}"
                )
                
    except Exception as e:
        return AudioTranscriptionResponse(
            text="",
            success=False,
            error_message=str(e)
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 