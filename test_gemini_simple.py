#!/usr/bin/env python3
"""
Teste simples da API do Gemini
"""

import httpx
import asyncio

GEMINI_API_KEY = "AIzaSyBu2oagQERfHTyrWLfvWJ1r-434jGS_4ts"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"

async def test_gemini_api():
    """Testa a API do Gemini diretamente"""
    print("🧪 Testando API do Gemini...")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
                json={
                    "contents": [
                        {
                            "parts": [
                                {
                                    "text": "Olá, como você está? Responda em português brasileiro."
                                }
                            ]
                        }
                    ]
                },
                timeout=30.0
            )
            
            print(f"Status Code: {response.status_code}")
            print(f"Headers: {response.headers}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"Resposta completa: {data}")
                
                if "candidates" in data and len(data["candidates"]) > 0:
                    text = data["candidates"][0]["content"]["parts"][0]["text"]
                    print(f"✅ Sucesso: {text}")
                else:
                    print("❌ Não encontrou 'candidates' na resposta")
            else:
                print(f"❌ Erro: {response.text}")
                
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_gemini_api()) 