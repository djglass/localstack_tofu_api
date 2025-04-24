# 🧠 LocalStack Tofu LLM API

This project builds a fully local, serverless API powered by:

- 🧪 **OpenTofu** — infrastructure-as-code
- ☁️ **LocalStack** — emulated AWS Lambda + API Gateway
- 🧠 **Ollama** — local LLM runtime (e.g. Llama3)
- 🐍 **Python** — Lambda backend using `requests`

## 🚀 Quickstart

### 1. Start LocalStack + Ollama

```bash
localstack start -d
ollama serve &
ollama pull llama3

