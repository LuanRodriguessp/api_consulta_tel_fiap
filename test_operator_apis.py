#!/usr/bin/env python3
"""
Script para testar diferentes APIs e sites de consulta de operadoras
"""

import requests
import time
import json

def test_abr_telecom_site():
    """Testa o site oficial da ABR Telecom"""
    print("🔍 Testando site oficial da ABR Telecom...")
    
    url = "https://consultanumero.abrtelecom.com.br/consultanumero/consulta/consultaSituacaoAtualCtg"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        # Primeira requisição para obter a página
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=10)
        
        print(f"   Status: {response.status_code}")
        print(f"   Tamanho da resposta: {len(response.text)} caracteres")
        
        # Verifica se há reCAPTCHA
        if 'recaptcha' in response.text.lower():
            print("   ⚠️  Detectado reCAPTCHA - Site tem proteção anti-bot")
        
        # Verifica se há outros elementos de proteção
        if 'cloudflare' in response.text.lower():
            print("   ⚠️  Detectado Cloudflare - Possível proteção adicional")
        
        # Salva a resposta para análise
        with open('abr_telecom_response.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print("   📄 Resposta salva em 'abr_telecom_response.html'")
        
        return response.status_code == 200
        
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False

def test_alternative_sites():
    """Testa sites alternativos de consulta"""
    print("\n🔍 Testando sites alternativos...")
    
    sites = [
        {
            "name": "Anatel - Consulta de Operadoras",
            "url": "https://www.gov.br/anatel/pt-br/assuntos/regulacao/operadoras",
            "description": "Site oficial da ANATEL"
        },
        {
            "name": "Teleco - Consulta de Operadoras",
            "url": "https://www.teleco.com.br/operadoras.asp",
            "description": "Portal de telecomunicações"
        },
        {
            "name": "Ministério das Comunicações",
            "url": "https://www.gov.br/mcom/pt-br",
            "description": "Site oficial do Ministério"
        }
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for site in sites:
        print(f"\n   📡 Testando: {site['name']}")
        print(f"   URL: {site['url']}")
        print(f"   Descrição: {site['description']}")
        
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

def test_free_apis():
    """Testa APIs gratuitas de consulta de números"""
    print("\n🔍 Testando APIs gratuitas...")
    
    apis = [
        {
            "name": "NumVerify API",
            "url": "http://apilayer.net/api/validate",
            "description": "API gratuita com limitações",
            "requires_key": True
        },
        {
            "name": "Abstract API",
            "url": "https://phonevalidation.abstractapi.com/v1/",
            "description": "API de validação de telefone",
            "requires_key": True
        },
        {
            "name": "HLRLookup",
            "url": "https://www.hlr-lookups.com/",
            "description": "API de lookup de números",
            "requires_key": True
        }
    ]
    
    for api in apis:
        print(f"\n   🔌 API: {api['name']}")
        print(f"   URL: {api['url']}")
        print(f"   Descrição: {api['description']}")
        
        if api['requires_key']:
            print("   🔑 Requer chave de API")
            print("   💡 Para usar: Registre-se gratuitamente e obtenha uma chave")
        else:
            print("   ✅ Gratuita sem chave")

def test_local_mapping():
    """Testa o mapeamento local de operadoras"""
    print("\n🔍 Testando mapeamento local...")
    
    from phone_validator import PhoneValidator
    
    validator = PhoneValidator()
    
    test_numbers = [
        "11988776655",  # São Paulo
        "21987654321",  # Rio de Janeiro
        "31987654321",  # Minas Gerais
        "41987654321",  # Paraná
        "51987654321",  # Rio Grande do Sul
    ]
    
    for number in test_numbers:
        result = validator._get_operator_from_local_mapping(number)
        print(f"\n   📞 {number}: {result['name']}")
        print(f"   Fonte: {result['api_source']}")
        print(f"   Confiança: {result.get('confidence', 'N/A')}")

def main():
    """Função principal"""
    print("🚀 Testando APIs e Sites de Consulta de Operadoras")
    print("=" * 60)
    
    # Testa o site oficial da ABR Telecom
    test_abr_telecom_site()
    
    # Testa sites alternativos
    test_alternative_sites()
    
    # Testa APIs gratuitas
    test_free_apis()
    
    # Testa mapeamento local
    test_local_mapping()
    
    print("\n" + "=" * 60)
    print("📋 Resumo das Opções:")
    print("1. ABR Telecom: Site oficial, mas com proteções anti-bot")
    print("2. APIs Gratuitas: Requerem registro e chave de API")
    print("3. Mapeamento Local: Baseado em padrões conhecidos (menos preciso)")
    print("4. Sites Alternativos: Podem ter informações úteis")
    
    print("\n💡 Recomendações:")
    print("- Para produção: Use APIs pagas ou gratuitas com chave")
    print("- Para desenvolvimento: Use mapeamento local")
    print("- Para máxima precisão: Combine múltiplas fontes")

if __name__ == "__main__":
    main() 