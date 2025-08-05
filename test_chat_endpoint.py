#!/usr/bin/env python3
"""
Teste do endpoint de chat
"""

import requests
import json

API_BASE_URL = "http://localhost:8000"

def test_chat():
    """Testa o endpoint de chat"""
    print("🧪 Testando endpoint de chat...")
    
    test_message = "Olá, como você está?"
    
    try:
        response = requests.post(
            f"{API_BASE_URL}/chat",
            json={"message": test_message},
            timeout=30
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Resposta: {data}")
            
            if data.get("success"):
                print(f"✅ Sucesso: {data['response']}")
            else:
                print(f"❌ Erro: {data.get('error_message', 'Erro desconhecido')}")
        else:
            print(f"❌ Status code: {response.status_code}")
            print(f"Resposta: {response.text}")
            
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_chat() 