# API de Validação de Celular Brasileiro + Chatbot

Uma API REST desenvolvida em Python usando FastAPI para validar números de celular brasileiros, formatá-los automaticamente, consultar operadoras e fornecer um chatbot inteligente com suporte a gravação de áudio usando a API do Google Gemini.

## 🚀 Funcionalidades

### 📞 Validação de Celular
- ✅ Validação de números de celular brasileiros
- ✅ Formatação automática no padrão `55 11 98877 6655`
- ✅ Adição automática do código do país (55) quando necessário
- ✅ Validação de DDD (11-99)
- ✅ Suporte a múltiplos formatos de entrada
- ✅ Consulta de operadora via site oficial da ABR Telecom

### 🤖 Chatbot Inteligente
- ✅ Chat por texto com respostas inteligentes
- ✅ Gravação de áudio em tempo real
- ✅ Transcrição automática de áudio para texto
- ✅ Integração com API do Google Gemini
- ✅ Respostas especializadas em validação de celular
- ✅ Interface moderna e responsiva


## 📋 Requisitos

- Python 3.8+
- FastAPI
- Uvicorn
- Requests

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd criacao_api
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a API:
```bash
python main.py
```

Ou usando uvicorn diretamente:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 📖 Como Usar

### Endpoints Disponíveis

#### 1. Validação via POST
**URL:** `POST /validate`

**Body:**
```json
{
    "phone_number": "11988776655"
}
```

**Resposta de Sucesso:**
```json
{
    "original_number": "11988776655",
    "formatted_number": "55 11 98877 6655",
    "is_valid": true,
    "country_code": "55",
    "area_code": "11",
         "number": "988776655",
     "operator": "Operadora encontrada (verificar no site)",
     "operator_info": {
         "name": "Operadora encontrada (verificar no site)",
         "ddd": "11",
         "number": "988776655",
         "type": "mobile",
         "country": "Brazil",
         "api_source": "ABR Telecom (Site Oficial)",
         "consult_url": "https://consultanumero.abrtelecom.com.br/consultanumero/consulta/consultaSituacaoAtualCtg?numero=11988776655",
         "status": "Consulta realizada com sucesso"
     },
     "error_message": null
}
```

#### 2. Validação via GET
**URL:** `GET /validate/{phone_number}`

**Exemplo:** `GET /validate/11988776655`

#### 3. Status da API
**URL:** `GET /health`

#### 4. Exemplos de Uso
**URL:** `GET /examples`

#### 5. Chatbot - Chat por Texto
**URL:** `POST /chat`

**Body:**
```json
{
    "message": "Como validar um número de celular?"
}
```

**Resposta:**
```json
{
    "response": "Para validar um número de celular brasileiro, você pode usar nossa API...",
    "success": true,
    "error_message": null
}
```

#### 6. Chatbot - Transcrição de Áudio
**URL:** `POST /transcribe-audio`

**Body:**
```json
{
    "audio_data": "base64_encoded_audio_data"
}
```

**Resposta:**
```json
{
    "text": "Texto transcrito do áudio",
    "success": true,
    "error_message": null
}
```

### Formatos de Entrada Aceitos

A API aceita números nos seguintes formatos:

- `11988776655` (11 dígitos)
- `5511988776655` (13 dígitos)
- `11 98877 6655` (com espaços)
- `(11) 98877-6655` (com parênteses e hífen)
- `+55 11 98877 6655` (com código do país)

### Validações Realizadas

1. **Comprimento:** Entre 11 e 13 dígitos
2. **Código do País:** Adiciona automaticamente "55" se não presente
3. **DDD:** Valida se está entre 11 e 99
4. **Tipo de Linha:** Verifica se é celular (começa com 9 ou 8)
5. **Formato:** Formata automaticamente no padrão brasileiro
6. **Operadora:** Consulta a operadora no site oficial da ABR Telecom

## 🔍 Consulta de Operadora

A API identifica a operadora do número através de múltiplas fontes com estratégia de fallback inteligente:

### **Fontes de Consulta (em ordem de prioridade):**
1. **NumVerify API** - API externa gratuita (100 consultas/mês)
2. **Abstract API** - API externa gratuita (100 consultas/mês)
3. **ABR Telecom (Site Oficial)** - Consulta direta no site oficial
4. **Mapeamento Local** - Baseado em padrões conhecidos de DDD

### **Configuração de APIs Externas:**
Para obter dados mais precisos, configure as APIs externas:

1. **Registre-se gratuitamente:**
   - NumVerify: https://numverify.com/
   - Abstract API: https://www.abstractapi.com/phone-validation-api

2. **Configure as chaves no arquivo `config.py`:**
   ```python
   NUMVERIFY_API_KEY = "sua_chave_aqui"
   ABSTRACT_API_KEY = "sua_chave_aqui"
   ```

3. **Consulte `CONFIGURACAO_APIS.md` para instruções detalhadas**

### **Informações Retornadas:**
- **Nome da Operadora:** Identificação da prestadora de serviço
- **Fonte da Consulta:** API utilizada (NumVerify, Abstract, ABR Telecom, etc.)
- **Status:** Status da consulta realizada
- **Nível de Confiança:** Alta, Média ou Baixa
- **Tipo:** Tipo de linha (mobile/fixed)
- **País:** País de origem do número


## 📝 Exemplos de Uso

### cURL

```bash
# Validação via POST
curl -X POST "http://localhost:8000/validate" \
     -H "Content-Type: application/json" \
     -d '{"phone_number": "11988776655"}'

# Validação via GET
curl "http://localhost:8000/validate/11988776655"

# Status da API
curl "http://localhost:8000/health"
```

### Python

```python
import requests

# Validação via POST
response = requests.post(
    "http://localhost:8000/validate",
    json={"phone_number": "11988776655"}
)
result = response.json()
print(result)

# Validação via GET
response = requests.get("http://localhost:8000/validate/11988776655")
result = response.json()
print(result)
```

### JavaScript

```javascript
// Validação via POST
fetch('http://localhost:8000/validate', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        phone_number: '11988776655'
    })
})
.then(response => response.json())
.then(data => console.log(data));

// Validação via GET
fetch('http://localhost:8000/validate/11988776655')
.then(response => response.json())
.then(data => console.log(data));
```

## 🌐 Frontend Web + Chatbot

A API possui um frontend web moderno e responsivo com chatbot inteligente:

### **Opção 1: Abrir diretamente no navegador**
1. Abra o arquivo `frontend.html` no seu navegador
2. Certifique-se de que a API está rodando na porta 8000

### **Opção 2: Usar servidor HTTP (Recomendado)**
```bash
python serve_frontend.py
```
- Acesse: http://localhost:8080/frontend.html
- O navegador abrirá automaticamente

### **Funcionalidades do Frontend:**
- ✅ Interface moderna e responsiva
- ✅ Validação em tempo real
- ✅ Exemplos clicáveis para teste
- ✅ Status da API em tempo real
- ✅ Resultados detalhados com informações da operadora
- ✅ Suporte a múltiplos formatos de entrada
- ✅ **Chatbot inteligente com suporte a texto e áudio**
- ✅ **Gravação de áudio em tempo real**
- ✅ **Transcrição automática de áudio**
- ✅ **Respostas especializadas em validação de celular**

### **Como usar o Chatbot:**
1. **Chat por texto**: Digite sua mensagem e pressione Enter
2. **Chat por áudio**: Clique no botão de microfone, fale e clique novamente
3. **Perguntas sugeridas**:
   - "Como validar um número de celular?"
   - "Quais são os DDDs válidos no Brasil?"
   - "Como funciona a API de validação?"
   - "Olá, tudo bem?"

## 📚 Documentação da API

Após iniciar o servidor, acesse a documentação interativa:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
- **Frontend:** http://localhost:8080/frontend.html (se usar servidor)

## 🧪 Testes

### Números Válidos
- `11988776655` → `55 11 98877 6655`
- `5511988776655` → `55 11 98877 6655`
- `11 98877 6655` → `55 11 98877 6655`
- `(11) 98877-6655` → `55 11 98877 6655`

### Números Inválidos
- `1234567890` (muito curto)
- `123456789012345` (muito longo)
- `11987654321` (não começa com 9)
- `5511987654321` (não começa com 9)

## 🔍 Estrutura do Projeto

```
criacao_api/
├── main.py                    # Arquivo principal da API
├── phone_validator.py         # Módulo de validação
├── requirements.txt           # Dependências
├── frontend.html             # Interface web com chatbot
├── serve_frontend.py         # Servidor HTTP para frontend
├── config.py                 # Configurações (APIs externas)
├── test_chatbot.py          # Testes do chatbot
├── test_gemini_simple.py    # Testes da API Gemini
├── test_chat_endpoint.py    # Testes do endpoint de chat
├── CHATBOT_GUIDE.md         # Guia de uso do chatbot
├── CONFIGURACAO_APIS.md     # Configuração de APIs externas
├── OPERADORAS_ANALISE.md    # Análise de fontes de operadora
├── test_api.py              # Testes gerais da API
├── test_frontend_errors.py  # Testes de erro do frontend
├── test_anatel_api.py       # Testes da API Anatel
├── test_real_api.py         # Testes de APIs reais
├── test_operator_apis.py    # Testes de APIs de operadora
├── abr_telecom_response.html # Resposta do site ABR Telecom
├── docker-compose.yml       # Configuração Docker Compose
├── Dockerfile               # Configuração Docker
└── README.md                # Documentação principal
```

## 🚀 Deploy

### Docker (Opcional)

Crie um `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Execute:
```bash
docker build -t phone-validation-api .
docker run -p 8000:8000 phone-validation-api
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Para dúvidas ou suporte, abra uma issue no repositório. 