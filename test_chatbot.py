#!/usr/bin/env python3
"""
Script de teste para verificar os endpoints do chatbot
"""

import requests
import json

API_BASE_URL = "http://localhost:8000"

def test_chat_endpoint():
    """Testa o endpoint de chat"""
    print("🧪 Testando endpoint de chat...")
    
    test_messages = [
        "Como validar um número de celular?",
        "Quais são os DDDs válidos no Brasil?",
        "Como funciona a API de validação?",
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
                    print(f"✅ Sucesso: {data['response'][:100]}...")
                else:
                    print(f"❌ Erro: {data.get('error_message', 'Erro desconhecido')}")
            else:
                print(f"❌ Status code: {response.status_code}")
                print(f"Resposta: {response.text}")
                
        except Exception as e:
            print(f"❌ Erro na requisição: {e}")

def test_health_endpoint():
    """Testa o endpoint de health"""
    print("\n🏥 Testando endpoint de health...")
    
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API está funcionando: {data}")
        else:
            print(f"❌ Status code: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Erro ao verificar health: {e}")

def test_validate_endpoint():
    """Testa o endpoint de validação"""
    print("\n📞 Testando endpoint de validação...")
    
    test_numbers = [
        "11988776655",
        "5511988776655",
        "11 98877 6655"
    ]
    
    for i, number in enumerate(test_numbers, 1):
        print(f"\n📱 Teste {i}: '{number}'")
        
        try:
            response = requests.post(
                f"{API_BASE_URL}/validate",
                json={"phone_number": number},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("is_valid"):
                    print(f"✅ Válido: {data['formatted_number']}")
                    print(f"   Operadora: {data.get('operator', 'N/A')}")
                else:
                    print(f"❌ Inválido: {data.get('error_message', 'Erro desconhecido')}")
            else:
                print(f"❌ Status code: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Erro na requisição: {e}")

def main():
    """Função principal"""
    print("🚀 Iniciando testes do chatbot...")
    print("=" * 50)
    
    # Testa health primeiro
    test_health_endpoint()
    
    # Testa validação
    test_validate_endpoint()
    
    # Testa chat
    test_chat_endpoint()
    
    print("\n" + "=" * 50)
    print("✨ Testes concluídos!")
    print("\n💡 Para testar o frontend:")
    print("   - Acesse: http://localhost:8080/frontend.html")
    print("   - Teste a validação de números")
    print("   - Teste o chatbot com texto e áudio")

if __name__ == "__main__":
    main() 