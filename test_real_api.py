#!/usr/bin/env python3
"""
Script para testar APIs reais de consulta de operadoras
"""

import requests
import json

def test_numverify_api():
    """Testa a API NumVerify (gratuita com limitações)"""
    print("🔍 Testando API NumVerify...")
    
    # Esta é uma chave de exemplo - você precisaria se registrar em https://numverify.com/
    # API_KEY = "sua_chave_aqui"
    
    # Como não temos chave real, vamos simular
    print("   ⚠️  Chave de API necessária")
    print("   💡 Registre-se em: https://numverify.com/")
    print("   📋 Plano gratuito: 100 consultas/mês")
    
    # Exemplo de como seria a chamada
    api_url = "http://apilayer.net/api/validate"
    params = {
        'access_key': 'YOUR_API_KEY',
        'number': '11988776655',
        'country_code': 'BR',
        'format': 1
    }
    
    print(f"   🔗 URL de exemplo: {api_url}")
    print(f"   📝 Parâmetros: {params}")
    
    return False

def test_abstract_api():
    """Testa a API Abstract (gratuita com limitações)"""
    print("\n🔍 Testando API Abstract...")
    
    print("   ⚠️  Chave de API necessária")
    print("   💡 Registre-se em: https://www.abstractapi.com/phone-validation-api")
    print("   📋 Plano gratuito: 100 consultas/mês")
    
    # Exemplo de como seria a chamada
    api_url = "https://phonevalidation.abstractapi.com/v1/"
    params = {
        'api_key': 'YOUR_API_KEY',
        'phone': '11988776655'
    }
    
    print(f"   🔗 URL de exemplo: {api_url}")
    print(f"   📝 Parâmetros: {params}")
    
    return False

def test_hlr_lookup():
    """Testa a API HLR Lookup"""
    print("\n🔍 Testando API HLR Lookup...")
    
    print("   ⚠️  Chave de API necessária")
    print("   💡 Registre-se em: https://www.hlr-lookups.com/")
    print("   📋 Plano gratuito: 100 consultas/mês")
    
    # Exemplo de como seria a chamada
    api_url = "https://www.hlr-lookups.com/api/v1/msisdn/5511988776655"
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY'
    }
    
    print(f"   🔗 URL de exemplo: {api_url}")
    print(f"   📝 Headers: {headers}")
    
    return False

def test_free_alternatives():
    """Testa alternativas gratuitas sem chave"""
    print("\n🔍 Testando alternativas gratuitas...")
    
    # 1. Testa um site que pode ter informações
    print("   📡 Testando sites com informações de operadoras...")
    
    sites = [
        {
            "name": "Wikipedia - Operadoras do Brasil",
            "url": "https://pt.wikipedia.org/wiki/Operadoras_de_telecomunicações_do_Brasil",
            "description": "Informações sobre operadoras brasileiras"
        },
        {
            "name": "Anatel - Lista de Prestadoras",
            "url": "https://www.gov.br/anatel/pt-br/assuntos/regulacao/prestadoras",
            "description": "Lista oficial de prestadoras"
        }
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    for site in sites:
        print(f"\n   🔗 Testando: {site['name']}")
        try:
            response = requests.get(site['url'], headers=headers, timeout=10)
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                print(f"   ✅ Acessível")
                if 'operadora' in response.text.lower() or 'prestadora' in response.text.lower():
                    print("   📋 Contém informações sobre operadoras")
            else:
                print(f"   ❌ Não acessível")
                
        except Exception as e:
            print(f"   ❌ Erro: {e}")

def test_local_enhanced_mapping():
    """Testa mapeamento local melhorado"""
    print("\n🔍 Testando mapeamento local melhorado...")
    
    from phone_validator import PhoneValidator
    
    validator = PhoneValidator()
    
    # Testa com números reais conhecidos
    test_cases = [
        {
            "number": "11988776655",
            "expected": "Vivo",
            "region": "São Paulo"
        },
        {
            "number": "21987654321", 
            "expected": "Claro",
            "region": "Rio de Janeiro"
        },
        {
            "number": "31987654321",
            "expected": "TIM", 
            "region": "Minas Gerais"
        },
        {
            "number": "41987654321",
            "expected": "Vivo",
            "region": "Paraná"
        },
        {
            "number": "51987654321",
            "expected": "TIM",
            "region": "Rio Grande do Sul"
        }
    ]
    
    for case in test_cases:
        result = validator._get_operator_from_local_mapping(case["number"])
        print(f"\n   📞 {case['number']} ({case['region']})")
        print(f"   Esperado: {case['expected']}")
        print(f"   Obtido: {result['name']}")
        print(f"   Confiança: {result.get('confidence', 'N/A')}")
        
        if result['name'] == case['expected']:
            print("   ✅ Correto!")
        else:
            print("   ❌ Incorreto")

def main():
    """Função principal"""
    print("🚀 Testando APIs Reais de Consulta de Operadoras")
    print("=" * 60)
    
    # Testa APIs que requerem chave
    test_numverify_api()
    test_abstract_api()
    test_hlr_lookup()
    
    # Testa alternativas gratuitas
    test_free_alternatives()
    
    # Testa mapeamento local melhorado
    test_local_enhanced_mapping()
    
    print("\n" + "=" * 60)
    print("📋 Conclusões:")
    print("1. APIs Pagas/Gratuitas: Mais precisas, mas requerem chave")
    print("2. Site ABR Telecom: Tem reCAPTCHA, difícil de automatizar")
    print("3. Mapeamento Local: Funciona, mas não é 100% preciso")
    print("4. Sites Informativos: Podem fornecer dados para melhorar mapeamento")
    
    print("\n💡 Próximos Passos:")
    print("- Registre-se em uma API gratuita para testes reais")
    print("- Melhore o mapeamento local com mais dados")
    print("- Implemente cache para consultas repetidas")
    print("- Considere usar múltiplas fontes para maior precisão")

if __name__ == "__main__":
    main() 