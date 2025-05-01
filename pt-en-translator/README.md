# 🌍 Tradutor EN ↔ PT com Hugging Face e Gradio

Este projeto é um tradutor bilíngue entre **Inglês** e **Português**, utilizando dois modelos distintos da Hugging Face: MarianMT e T5, com uma interface gráfica simples em Gradio.

## 🧠 Tecnologias utilizadas

- [Transformers (Hugging Face)](https://huggingface.co/docs/transformers)
- [Gradio](https://www.gradio.app/)
- Python 3.8+

## 🚀 Como executar localmente

```bash
git clone https://github.com/seu-usuario/pt-en-translator.git
cd pt-en-translator

# (opcional)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
python interface.py
```
## ✅ Funcionalidades

Tradução de Inglês para Português com MarianMT.

Tradução de Português para Inglês com T5.

Interface simples e interativa com Gradio.

Botão para limpar os campos de texto.

## 🌐 Execução no Google Colab

Também funciona no Google Colab! Basta copiar os arquivos interface.py e translator.py e executar após instalar os pacotes:

!pip install transformers gradio torch

## 📃 Licença
Este projeto está licenciado sob a MIT License.
