#!/usr/bin/env python3
"""
Script de teste para a API de Validação de Celular
Demonstra como usar a API e testa diferentes cenários
"""

import requests
import json
import time

# Configuração da API
BASE_URL = "http://localhost:8000"

def test_api_health():
    """Testa o endpoint de health check"""
    print("🔍 Testando health check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ API está funcionando!")
            print(f"   Status: {response.json()}")
        else:
            print(f"❌ Erro no health check: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro ao conectar com a API: {e}")

def test_phone_validation_post(phone_number):
    """Testa validação via POST"""
    print(f"\n📞 Testando validação POST: {phone_number}")
    try:
        response = requests.post(
            f"{BASE_URL}/validate",
            json={"phone_number": phone_number},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            if result["is_valid"]:
                print(f"✅ Válido: {result['formatted_number']}")
                print(f"   País: {result['country_code']}")
                print(f"   DDD: {result['area_code']}")
                print(f"   Operadora: {result.get('operator', 'N/A')}")
            else:
                print(f"❌ Inválido: {result['error_message']}")
        else:
            print(f"❌ Erro na requisição: {response.status_code}")
            print(f"   Resposta: {response.text}")
    except Exception as e:
        print(f"❌ Erro: {e}")

def test_phone_validation_get(phone_number):
    """Testa validação via GET"""
    print(f"\n📞 Testando validação GET: {phone_number}")
    try:
        response = requests.get(f"{BASE_URL}/validate/{phone_number}")
        
        if response.status_code == 200:
            result = response.json()
            if result["is_valid"]:
                print(f"✅ Válido: {result['formatted_number']}")
                print(f"   Operadora: {result.get('operator', 'N/A')}")
            else:
                print(f"❌ Inválido: {result['error']}")
        else:
            print(f"❌ Erro na requisição: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro: {e}")

def test_examples():
    """Testa o endpoint de exemplos"""
    print("\n📋 Obtendo exemplos...")
    try:
        response = requests.get(f"{BASE_URL}/examples")
        if response.status_code == 200:
            examples = response.json()
            print("✅ Exemplos obtidos:")
            print(f"   Formato esperado: {examples['expected_format']}")
            print(f"   Válidos: {examples['valid_examples']}")
            print(f"   Inválidos: {examples['invalid_examples']}")
        else:
            print(f"❌ Erro ao obter exemplos: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro: {e}")

def run_comprehensive_tests():
    """Executa testes abrangentes"""
    print("🚀 Iniciando testes da API de Validação de Celular")
    print("=" * 50)
    
    # Teste de health check
    test_api_health()
    
    # Teste de exemplos
    test_examples()
    
    # Testes com números válidos
    valid_numbers = [
        "11988776655",
        "5511988776655", 
        "11 98877 6655",
        "(11) 98877-6655",
        "+55 11 98877 6655",
        "21987654321",
        "31987654321"
    ]
    
    print("\n" + "=" * 50)
    print("🧪 Testando números VÁLIDOS")
    print("=" * 50)
    
    for number in valid_numbers:
        test_phone_validation_post(number)
        time.sleep(0.5)  # Pequena pausa entre requisições
    
    # Testes com números inválidos
    invalid_numbers = [
        "1234567890",      # Muito curto
        "123456789012345", # Muito longo
        "11987654321",     # Não começa com 9
        "5511987654321",   # Não começa com 9
        "12345678901",     # DDD inválido
        "abc123def456"     # Caracteres não numéricos
    ]
    
    print("\n" + "=" * 50)
    print("🧪 Testando números INVÁLIDOS")
    print("=" * 50)
    
    for number in invalid_numbers:
        test_phone_validation_post(number)
        time.sleep(0.5)
    
    # Testes GET
    print("\n" + "=" * 50)
    print("🧪 Testando endpoint GET")
    print("=" * 50)
    
    test_numbers = ["11988776655", "1234567890", "21987654321"]
    for number in test_numbers:
        test_phone_validation_get(number)
        time.sleep(0.5)

def interactive_test():
    """Modo interativo para testar números"""
    print("\n🎯 Modo Interativo")
    print("Digite números de telefone para testar (ou 'sair' para encerrar)")
    
    while True:
        phone_number = input("\n📞 Digite um número: ").strip()
        
        if phone_number.lower() in ['sair', 'exit', 'quit']:
            print("👋 Encerrando...")
            break
        
        if not phone_number:
            continue
        
        test_phone_validation_post(phone_number)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_test()
    else:
        run_comprehensive_tests()
        
    print("\n" + "=" * 50)
    print("✨ Testes concluídos!")
    print("📚 Acesse http://localhost:8000/docs para documentação interativa") 