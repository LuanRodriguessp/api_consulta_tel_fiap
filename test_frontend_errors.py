#!/usr/bin/env python3
"""
Script para testar cenários de erro que podem causar [object Object] no frontend
"""

import requests
import json

def test_error_scenarios():
    """Testa diferentes cenários de erro para verificar se o frontend os trata corretamente"""
    
    base_url = "http://localhost:8000"
    
    print("🧪 Testando cenários de erro do frontend")
    print("=" * 50)
    
    # Teste 1: Número muito curto (deve retornar erro de validação Pydantic)
    print("\n📞 Teste 1: Número muito curto")
    try:
        response = requests.post(
            f"{base_url}/validate",
            json={"phone_number": "123"},
            headers={"Content-Type": "application/json"}
        )
        print(f"Status: {response.status_code}")
        print(f"Resposta: {response.text}")
        
        if response.status_code == 422:
            data = response.json()
            print("✅ Erro de validação Pydantic detectado corretamente")
            print(f"   Detail type: {type(data.get('detail'))}")
            if isinstance(data.get('detail'), list):
                print(f"   Detail é array com {len(data['detail'])} itens")
                for i, error in enumerate(data['detail']):
                    print(f"   Erro {i+1}: {error.get('msg', 'Sem mensagem')}")
        else:
            print("❌ Status inesperado")
            
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
    
    # Teste 2: Número muito longo
    print("\n📞 Teste 2: Número muito longo")
    try:
        response = requests.post(
            f"{base_url}/validate",
            json={"phone_number": "12345678901234567890"},
            headers={"Content-Type": "application/json"}
        )
        print(f"Status: {response.status_code}")
        print(f"Resposta: {response.text}")
        
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
    
    # Teste 3: Número com caracteres não numéricos
    print("\n📞 Teste 3: Número com caracteres especiais")
    try:
        response = requests.post(
            f"{base_url}/validate",
            json={"phone_number": "abc123def456"},
            headers={"Content-Type": "application/json"}
        )
        print(f"Status: {response.status_code}")
        print(f"Resposta: {response.text}")
        
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
    
    # Teste 4: Número válido mas que falha na validação interna
    print("\n📞 Teste 4: Número com formato inválido")
    try:
        response = requests.post(
            f"{base_url}/validate",
            json={"phone_number": "12345678901"},  # 11 dígitos mas não começa com 9
            headers={"Content-Type": "application/json"}
        )
        print(f"Status: {response.status_code}")
        print(f"Resposta: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            if not data.get('is_valid'):
                print("✅ Erro de validação interna detectado corretamente")
                print(f"   Error message: {data.get('error_message')}")
            else:
                print("❌ Número foi considerado válido quando deveria ser inválido")
        else:
            print("❌ Status inesperado")
            
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
    
    # Teste 5: Número válido para comparação
    print("\n📞 Teste 5: Número válido (para comparação)")
    try:
        response = requests.post(
            f"{base_url}/validate",
            json={"phone_number": "11988776655"},
            headers={"Content-Type": "application/json"}
        )
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('is_valid'):
                print("✅ Número válido processado corretamente")
                print(f"   Formatted: {data.get('formatted_number')}")
                print(f"   Operator: {data.get('operator')}")
            else:
                print("❌ Número válido foi rejeitado")
        else:
            print("❌ Status inesperado para número válido")
            
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
    
    print("\n" + "=" * 50)
    print("✅ Testes de erro concluídos!")
    print("\n💡 Verifique no frontend se as mensagens de erro são exibidas corretamente")
    print("   e não aparecem mais como [object Object]")

if __name__ == "__main__":
    test_error_scenarios() 