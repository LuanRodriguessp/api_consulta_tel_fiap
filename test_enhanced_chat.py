#!/usr/bin/env python3
"""
Teste do chatbot melhorado com validação automática
"""

import requests
import json

API_BASE_URL = "http://localhost:8000"

def test_enhanced_chat():
    """Testa o chatbot com perguntas sobre números específicos"""
    print("🧪 Testando chatbot melhorado...")
    
    test_messages = [
        "O número de celular 11953234369 é válido?",
        "Como validar o número 11988776655?",
        "O número 1234567890 é válido?",
        "Quais são os DDDs válidos no Brasil?",
        "Olá, tudo bem?"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n📝 Teste {i}: '{message}'")
        
        try:
            response = requests.post(
                f"{API_BASE_URL}/chat",
                json={"message": message},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    print(f"✅ Resposta: {data['response'][:200]}...")
                else:
                    print(f"❌ Erro: {data.get('error_message', 'Erro desconhecido')}")
            else:
                print(f"❌ Status code: {response.status_code}")
                print(f"Resposta: {response.text}")
                
        except Exception as e:
            print(f"❌ Erro na requisição: {e}")

if __name__ == "__main__":
    test_enhanced_chat() 