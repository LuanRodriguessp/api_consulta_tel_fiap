#!/usr/bin/env python3
"""
Configuração para APIs externas de consulta de operadoras
"""

# =============================================================================
# CONFIGURAÇÃO DAS APIs EXTERNAS
# =============================================================================

# API NumVerify (gratuita para 100 consultas/mês)
# Registre-se em: https://numverify.com/
NUMVERIFY_API_KEY = None  # Configure sua chave aqui

# API Abstract (gratuita para 100 consultas/mês)
# Registre-se em: https://www.abstractapi.com/phone-validation-api
ABSTRACT_API_KEY = None  # Configure sua chave aqui

# =============================================================================
# INSTRUÇÕES DE CONFIGURAÇÃO
# =============================================================================

"""
Para usar as APIs externas de consulta de operadoras:

1. NUMVERIFY API:
   - Acesse: https://numverify.com/
   - Registre-se gratuitamente
   - Obtenha sua chave API
   - Configure: NUMVERIFY_API_KEY = "sua_chave_aqui"

2. ABSTRACT API:
   - Acesse: https://www.abstractapi.com/phone-validation-api
   - Registre-se gratuitamente
   - Obtenha sua chave API
   - Configure: ABSTRACT_API_KEY = "sua_chave_aqui"

3. VANTAGENS DAS APIs EXTERNAS:
   - ✅ Dados mais precisos e atualizados
   - ✅ Considera portabilidade de números
   - ✅ Informações detalhadas sobre operadoras
   - ✅ 100 consultas gratuitas por mês

4. SEM APIs CONFIGURADAS:
   - ✅ Sistema funciona com mapeamento local
   - ✅ ABR Telecom como fonte alternativa
   - ✅ Fallback para identificação por DDD
   - ✅ Sem custos ou limites de consulta

5. EXEMPLO DE USO:
   ```python
   # Com APIs configuradas
   NUMVERIFY_API_KEY = "abc123def456"
   ABSTRACT_API_KEY = "xyz789uvw012"
   
   # Sem APIs (funciona normalmente)
   NUMVERIFY_API_KEY = None
   ABSTRACT_API_KEY = None
   ```
"""

# =============================================================================
# CONFIGURAÇÃO DE FONTES DE CONSULTA
# =============================================================================

# Ordem de prioridade para consulta de operadoras
CONSULTATION_PRIORITY = [
    "numverify_api",      # 1º: NumVerify API (se configurada)
    "abstract_api",       # 2º: Abstract API (se configurada)
    "abr_telecom",        # 3º: ABR Telecom (site oficial)
    "local_mapping"       # 4º: Mapeamento local (fallback)
]

# Timeout para requisições externas (em segundos)
REQUEST_TIMEOUT = 10

# Número máximo de tentativas para APIs externas
MAX_RETRIES = 3

# =============================================================================
# CONFIGURAÇÃO DE LOGS
# =============================================================================

# Habilitar logs detalhados
ENABLE_DETAILED_LOGS = True

# Log de consultas de operadoras
LOG_OPERATOR_QUERIES = True

# Log de erros de APIs externas
LOG_API_ERRORS = True 