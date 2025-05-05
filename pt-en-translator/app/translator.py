# Importa as bibliotecas necessárias da Hugging Face
from transformers import MarianMTModel, MarianTokenizer, T5Tokenizer, T5ForConditionalGeneration

# Define a classe Translator que encapsula os modelos de tradução
class Translator:
    def __init__(self):
        # Mensagem de carregamento
        print("Carregando modelos...")

        # Nomes dos modelos da Hugging Face
        self.model_en_pt_name = 'Helsinki-NLP/opus-mt-tc-big-en-pt'   # Modelo para Inglês → Português
        self.model_pt_en_name = 'unicamp-dl/translation-pt-en-t5'   # Modelo para Português → Inglês

        # Carrega o modelo e tokenizer para tradução EN → PT
        tokenizer_en_pt = MarianTokenizer.from_pretrained(model_en_pt_name)
        model_en_pt = MarianMTModel.from_pretrained(model_en_pt_name)

        # Carrega o modelo e tokenizer para tradução PT → EN
        tokenizer_pt_en = T5Tokenizer.from_pretrained(model_pt_en_name)  # Usando T5Tokenizer para o modelo T5
        model_pt_en = T5ForConditionalGeneration.from_pretrained(model_pt_en_name)  # Usando T5ForConditionalGeneration para PT → EN

        # Confirma que tudo foi carregado
        print("Modelos carregados com sucesso!")

    # Função principal de tradução
    def traduzir(texto, direcao):
        # Verifica se o texto está vazio
        if not texto.strip():
            return "Entrada vazia."

        # Divide o texto em linhas/frases
        frases = [linha.strip() for linha in texto.split('\n') if linha.strip()]

        # Seleciona modelo e tokenizer com base na direção da tradução
        if direcao == "Inglês → Português":
            tokenizer, model = tokenizer_en_pt, model_en_pt
        elif direcao == "Português → Inglês":
            tokenizer, model = tokenizer_pt_en, model_pt_en
        else:
            return "❌ Direção de tradução inválida."

        # Tokeniza as frases para entrada no modelo
         tokens = tokenizer(frases, return_tensors="pt", padding=True, truncation=True)

        # Gera a tradução
        saida = model.generate(**tokens)

        # Decodifica os resultados em texto legível
        traducao = tokenizer.batch_decode(saida, skip_special_tokens=True)

        # Junta as frases traduzidas com quebras de linha
        return '\n'.join(traducao)
