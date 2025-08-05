# 🔧 Configuração de APIs Externas para Consulta de Operadoras

## 📋 **Visão Geral**

A API de validação de celular brasileiro agora suporta múltiplas fontes para consulta de operadoras, incluindo APIs externas que fornecem dados mais precisos e atualizados.

## 🎯 **Fontes de Consulta Disponíveis**

### 1. **APIs Externas (Recomendadas)**
- **NumVerify API** - 100 consultas gratuitas/mês
- **Abstract API** - 100 consultas gratuitas/mês

### 2. **Fontes Alternativas**
- **ABR Telecom** - Site oficial (com limitações)
- **Mapeamento Local** - Baseado em padrões de DDD

## 🚀 **Como Configurar as APIs Externas**

### **Passo 1: Registrar-se nas APIs**

#### **NumVerify API**
1. Acesse: https://numverify.com/
2. Clique em "Get Free API Key"
3. Preencha o formulário de registro
4. Confirme seu email
5. Copie sua chave API

#### **Abstract API**
1. Acesse: https://www.abstractapi.com/phone-validation-api
2. Clique em "Get Started for Free"
3. Crie uma conta gratuita
4. Acesse o dashboard
5. Copie sua chave API

### **Passo 2: Configurar as Chaves**

Edite o arquivo `config.py`:

```python
# API NumVerify (gratuita para 100 consultas/mês)
NUMVERIFY_API_KEY = "sua_chave_numverify_aqui"

# API Abstract (gratuita para 100 consultas/mês)
ABSTRACT_API_KEY = "sua_chave_abstract_aqui"
```

### **Passo 3: Testar a Configuração**

Execute o script de teste:

```bash
python test_api.py
```

## 📊 **Comparação das Fontes**

| Fonte | Precisão | Limite | Custo | Portabilidade |
|-------|----------|--------|-------|---------------|
| **NumVerify API** | ⭐⭐⭐⭐⭐ | 100/mês | Gratuito | ✅ |
| **Abstract API** | ⭐⭐⭐⭐⭐ | 100/mês | Gratuito | ✅ |
| **ABR Telecom** | ⭐⭐⭐ | Ilimitado | Gratuito | ❌ |
| **Mapeamento Local** | ⭐⭐ | Ilimitado | Gratuito | ❌ |

## 🔄 **Estratégia de Consulta**

O sistema usa uma estratégia de fallback inteligente:

1. **Primeiro**: Tenta NumVerify API (se configurada)
2. **Segundo**: Tenta Abstract API (se configurada)
3. **Terceiro**: Tenta ABR Telecom (site oficial)
4. **Quarto**: Usa mapeamento local (fallback)

## 💡 **Exemplos de Uso**

### **Com APIs Configuradas**
```python
# config.py
NUMVERIFY_API_KEY = "abc123def456"
ABSTRACT_API_KEY = "xyz789uvw012"

# Resultado esperado
{
    "name": "Vivo",
    "api_source": "NumVerify API",
    "confidence": "Alta",
    "status": "Consulta bem-sucedida"
}
```

### **Sem APIs Configuradas**
```python
# config.py
NUMVERIFY_API_KEY = None
ABSTRACT_API_KEY = None

# Resultado esperado
{
    "name": "Vivo",
    "api_source": "Mapeamento Local (DDD)",
    "confidence": "Média",
    "status": "Identificação por padrão de DDD"
}
```

## 🛠️ **Configuração Avançada**

### **Timeout de Requisições**
```python
# config.py
REQUEST_TIMEOUT = 15  # segundos
```

### **Número de Tentativas**
```python
# config.py
MAX_RETRIES = 3
```

### **Logs Detalhados**
```python
# config.py
ENABLE_DETAILED_LOGS = True
LOG_OPERATOR_QUERIES = True
LOG_API_ERRORS = True
```

## 🔒 **Segurança**

### **Proteção de Chaves API**
- Nunca commite chaves API no Git
- Use variáveis de ambiente em produção
- Configure `.gitignore` para excluir `config.py`

### **Exemplo de Configuração Segura**
```python
import os

NUMVERIFY_API_KEY = os.getenv('NUMVERIFY_API_KEY')
ABSTRACT_API_KEY = os.getenv('ABSTRACT_API_KEY')
```

## 📈 **Monitoramento**

### **Verificar Uso das APIs**
- NumVerify: Dashboard em https://numverify.com/
- Abstract: Dashboard em https://www.abstractapi.com/

### **Logs de Consulta**
O sistema registra todas as consultas quando habilitado:
```python
# Exemplo de log
2024-01-15 10:30:15 - Consulta: 11988776655 → Vivo (NumVerify API)
2024-01-15 10:30:16 - Consulta: 21987654321 → Claro (Abstract API)
```

## 🚨 **Limitações e Considerações**

### **APIs Gratuitas**
- **Limite**: 100 consultas/mês
- **Rate Limit**: Varia por API
- **Precisão**: Muito alta
- **Portabilidade**: Considerada

### **Fontes Alternativas**
- **Limite**: Ilimitado
- **Precisão**: Média a baixa
- **Portabilidade**: Não considerada
- **Atualização**: Manual

## 🔧 **Solução de Problemas**

### **Erro: "API não configurada"**
```bash
# Verifique se as chaves estão configuradas
python -c "from config import NUMVERIFY_API_KEY; print(NUMVERIFY_API_KEY)"
```

### **Erro: "Rate limit exceeded"**
- Aguarde o próximo mês
- Considere upgrade para plano pago
- Use fontes alternativas temporariamente

### **Erro: "Timeout"**
```python
# Aumente o timeout
REQUEST_TIMEOUT = 20
```

## 📞 **Suporte**

### **NumVerify**
- Email: support@numverify.com
- Documentação: https://numverify.com/documentation

### **Abstract API**
- Email: support@abstractapi.com
- Documentação: https://www.abstractapi.com/docs

### **Projeto Local**
- Issues: GitHub do projeto
- Documentação: README.md

## 🎉 **Benefícios da Configuração**

✅ **Dados mais precisos** - APIs atualizadas em tempo real  
✅ **Portabilidade** - Considera mudanças de operadora  
✅ **Informações detalhadas** - Tipo de linha, país, etc.  
✅ **Alta confiabilidade** - Múltiplas fontes de backup  
✅ **Sem custos** - 100 consultas gratuitas por mês  
✅ **Fácil configuração** - Apenas adicione suas chaves API 