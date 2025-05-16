
# 📚 CrewAI: Gerador de Planos de Aula Inteligente

Este projeto utiliza **CrewAI**, **Python** e uma **LLM da Groq** para gerar automaticamente **planos de aula personalizados** para professores, com base em entradas como tema, série, duração e cabeçalho institucional. Ele também busca **recursos educacionais online** para enriquecer o plano.

## Funcionalidades

- Geração automática de planos de aula com base em tema, série e duração.
- Inclusão de cabeçalho com nome da escola e professor.
- Sugestões de recursos online (Wikipedia, DuckDuckGo, YouTube).
- Saída formatada em arquivos `.txt`.
- Geração de Arquivo ` .docx`.

## Pré-requisitos

- Python 3.12
- Conta na [Groq](https://console.groq.com/) para obter a chave da LLM
- (Opcional) Chave da [YouTube Data API](https://console.cloud.google.com/) para enriquecer os resultados

### Verifique sua versão do Python

```bash
python --version
```

## 📥 Instalação

### 1\. Clone o repositório

```bash
git clone https://github.com/Gabrielst9/crewai-api-main.git
cd crewai-api-main
```

### 2\. Configure ambiente virtual

```bash
py -3.12 -m venv venv
```

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3\. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4\. Configure as chaves de API

Crie um arquivo `.env` com o seguinte conteúdo:

```env
GROQ_API_KEY=sua_chave_groq_aqui

# APIs Educacionais
DUCKDUCKGO_API_URL=https://api.duckduckgo.com/
WIKIPEDIA_API_URL=https://pt.wikipedia.org/api/rest_v1/page/summary/
YOUTUBE_API_KEY=sua_chave_youtube_aqui
YOUTUBE_API_URL=https://www.googleapis.com/youtube/v3/search
```

## 🖥️ Como Usar

Execute o sistema principal:

```bash
python main.py
```

Você será guiado para inserir:
- Nome da escola
- Nome do professor
- Tema da aula
- Série ou ano
- Duração da aula

Ao final, serão gerados os arquivos formatados em `/output`:
- Plano de aula gerado
- Versão com cabeçalho formatado
- Recursos educacionais sugeridos

---

Desenvolvido por **Gabriel** • **2025**
