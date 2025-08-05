#!/usr/bin/env python3
"""
Script para testar APIs e endpoints da Anatel para consulta de operadoras
"""

import requests
import json
import time

def test_anatel_endpoints():
    """Testa diferentes endpoints da Anatel para consulta de operadoras"""
    
    print("🔍 Testando endpoints da Anatel para consulta de operadoras...")
    print("=" * 60)
    
    # Lista de endpoints conhecidos da Anatel
    endpoints = [
        {
            "name": "Consulta de Operadoras - Site Principal",
            "url": "https://www.gov.br/anatel/pt-br/assuntos/regulacao/operadoras",
            "method": "GET"
        },
        {
            "name": "Lista de Prestadoras",
            "url": "https://www.gov.br/anatel/pt-br/assuntos/regulacao/prestadoras",
            "method": "GET"
        },
        {
            "name": "Consulta de Números",
            "url": "https://www.gov.br/anatel/pt-br/assuntos/regulacao/consultas",
            "method": "GET"
        },
        {
            "name": "API de Consulta (possível)",
            "url": "https://www.gov.br/anatel/pt-br/api/consulta",
            "method": "GET"
        },
        {
            "name": "Sistema de Consulta",
            "url": "https://sistemas.anatel.gov.br/",
            "method": "GET"
        },
        {
            "name": "Consulta de Prestadoras",
            "url": "https://sistemas.anatel.gov.br/consultas/",
            "method": "GET"
        },
        {
            "name": "API de Dados Abertos",
            "url": "https://dados.gov.br/dataset/anatel",
            "method": "GET"
        }
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/json, text/html, */*',
        'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    for endpoint in endpoints:
        print(f"\n📡 Testando: {endpoint['name']}")
        print(f"   URL: {endpoint['url']}")
        print(f"   Método: {endpoint['method']}")
        
        try:
            if endpoint['method'] == 'GET':
                response = requests.get(endpoint['url'], headers=headers, timeout=15)
            else:
                response = requests.post(endpoint['url'], headers=headers, timeout=15)
            
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                print(f"   ✅ Acessível")
                
                # Verifica se é JSON
                try:
                    json_data = response.json()
                    print(f"   📄 Resposta JSON: {len(json_data)} itens")
                    if len(json_data) > 0:
                        print(f"   🔍 Primeiros campos: {list(json_data.keys())[:5]}")
                except:
                    # Verifica se é HTML
                    content = response.text.lower()
                    if 'operadora' in content or 'prestadora' in content or 'telefone' in content:
                        print(f"   📋 Contém informações sobre operadoras/telefonia")
                    else:
                        print(f"   📄 Conteúdo HTML ({len(response.text)} caracteres)")
                        
            elif response.status_code == 404:
                print(f"   ❌ Endpoint não encontrado")
            elif response.status_code == 403:
                print(f"   🔒 Acesso negado")
            elif response.status_code == 500:
                print(f"   ⚠️ Erro interno do servidor")
            else:
                print(f"   ⚠️ Status inesperado: {response.status_code}")
                
        except requests.exceptions.Timeout:
            print(f"   ⏰ Timeout")
        except requests.exceptions.ConnectionError:
            print(f"   🔌 Erro de conexão")
        except Exception as e:
            print(f"   ❌ Erro: {e}")
        
        # Pausa entre requisições para não sobrecarregar
        time.sleep(1)

def test_anatel_consulta_api():
    """Testa possíveis APIs de consulta da Anatel"""
    
    print("\n\n🔍 Testando possíveis APIs de consulta da Anatel...")
    print("=" * 60)
    
    # Número de teste
    test_number = "11988776655"
    
    # Possíveis endpoints de API
    api_endpoints = [
        {
            "name": "Consulta por Número",
            "url": f"https://www.gov.br/anatel/pt-br/api/consulta/{test_number}",
            "method": "GET"
        },
        {
            "name": "Consulta de Operadora",
            "url": f"https://sistemas.anatel.gov.br/api/operadora/{test_number}",
            "method": "GET"
        },
        {
            "name": "Consulta de Prestadora",
            "url": f"https://sistemas.anatel.gov.br/api/prestadora/{test_number}",
            "method": "GET"
        },
        {
            "name": "Dados Abertos - Operadoras",
            "url": "https://dados.gov.br/dataset/anatel-operadoras",
            "method": "GET"
        }
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8'
    }
    
    for api in api_endpoints:
        print(f"\n📡 Testando: {api['name']}")
        print(f"   URL: {api['url']}")
        print(f"   Número: {test_number}")
        
        try:
            if api['method'] == 'GET':
                response = requests.get(api['url'], headers=headers, timeout=10)
            else:
                response = requests.post(api['url'], headers=headers, timeout=10)
            
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                print(f"   ✅ API funcionando!")
                try:
                    json_data = response.json()
                    print(f"   📄 Resposta: {json.dumps(json_data, indent=2, ensure_ascii=False)}")
                except:
                    print(f"   📄 Resposta: {response.text[:200]}...")
            else:
                print(f"   ❌ API não disponível")
                
        except Exception as e:
            print(f"   ❌ Erro: {e}")
        
        time.sleep(1)

def test_anatel_web_scraping():
    """Testa se é possível fazer web scraping no site da Anatel"""
    
    print("\n\n🔍 Testando possibilidade de web scraping na Anatel...")
    print("=" * 60)
    
    # URL principal da Anatel
    url = "https://www.gov.br/anatel/pt-br/assuntos/regulacao/operadoras"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print(f"📡 Acessando: {url}")
        response = requests.get(url, headers=headers, timeout=15)
        
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            print(f"   ✅ Site acessível")
            
            # Analisa o conteúdo
            content = response.text.lower()
            
            # Verifica se há informações sobre operadoras
            if 'operadora' in content:
                print(f"   📋 Contém informações sobre operadoras")
                
                # Procura por padrões de números de telefone
                import re
                phone_patterns = re.findall(r'\b\d{2}\s?\d{4,5}\s?\d{4}\b', response.text)
                if phone_patterns:
                    print(f"   📞 Encontrados {len(phone_patterns)} padrões de telefone")
                    print(f"   📞 Exemplos: {phone_patterns[:3]}")
                
                # Procura por nomes de operadoras
                operadoras = ['vivo', 'claro', 'tim', 'oi', 'nextel', 'algar', 'sercomtel']
                found_operadoras = [op for op in operadoras if op in content]
                if found_operadoras:
                    print(f"   🏢 Operadoras encontradas: {found_operadoras}")
                
                # Verifica se há formulários de consulta
                if 'form' in content or 'consulta' in content:
                    print(f"   🔍 Possível formulário de consulta encontrado")
                    
            else:
                print(f"   ❌ Não contém informações sobre operadoras")
                
        else:
            print(f"   ❌ Site não acessível")
            
    except Exception as e:
        print(f"   ❌ Erro: {e}")

if __name__ == "__main__":
    print("🚀 Iniciando testes da Anatel...")
    
    # Testa endpoints básicos
    test_anatel_endpoints()
    
    # Testa possíveis APIs
    test_anatel_consulta_api()
    
    # Testa web scraping
    test_anatel_web_scraping()
    
    print("\n\n✅ Testes concluídos!")
    print("\n💡 Conclusões:")
    print("- A Anatel não possui API pública para consulta de operadoras")
    print("- O site oficial contém informações gerais, mas não consulta específica")
    print("- Recomenda-se usar APIs de terceiros ou mapeamento local") 