# Importa as bibliotecas necessárias da Hugging Face
from transformers import MarianMTModel, MarianTokenizer

# Define a classe Translator que encapsula os modelos de tradução
class Translator:
    def __init__(self):
        # Mensagem de carregamento
        print("Carregando modelos...")

        # Nomes dos modelos da Hugging Face
        self.model_en_pt_name = 'Helsinki-NLP/opus-mt-en-pt'   # Modelo para Inglês → Português
        self.model_pt_en_name = 'Helsinki-NLP/opus-mt-pt-en'   # Modelo para Português → Inglês

        # Carrega o modelo e tokenizer para tradução EN → PT
        self.tokenizer_en_pt = MarianTokenizer.from_pretrained(self.model_en_pt_name)
        self.model_en_pt = MarianMTModel.from_pretrained(self.model_en_pt_name)

        # Carrega o modelo e tokenizer para tradução PT → EN
        self.tokenizer_pt_en = MarianTokenizer.from_pretrained(self.model_pt_en_name)
        self.model_pt_en = MarianMTModel.from_pretrained(self.model_pt_en_name)

        # Confirma que tudo foi carregado
        print("Modelos carregados com sucesso!")

    # Função principal de tradução
    def translate(self, text, direction):
        # Verifica se o texto está vazio
        if not text.strip():
            return "Entrada vazia."

        # Divide o texto em linhas/frases
        lines = [linha.strip() for linha in text.split('\n') if linha.strip()]

        # Seleciona modelo e tokenizer com base na direção da tradução
        if direction == "Inglês → Português":
            tokenizer, model = self.tokenizer_en_pt, self.model_en_pt
        elif direction == "Português → Inglês":
            tokenizer, model = self.tokenizer_pt_en, self.model_pt_en
        else:
            return "❌ Direção de tradução inválida."

        # Tokeniza as frases para entrada no modelo
        inputs = tokenizer(lines, return_tensors="pt", padding=True, truncation=True)

        # Gera a tradução
        outputs = model.generate(**inputs)

        # Decodifica os resultados em texto legível
        translated = tokenizer.batch_decode(outputs, skip_special_tokens=True)

        # Junta as frases traduzidas com quebras de linha
        return '\n'.join(translated)
