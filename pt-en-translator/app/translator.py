from transformers import MarianMTModel, MarianTokenizer

class Translator:
    def __init__(self):
        print("Carregando modelos...")
        self.model_en_pt_name = 'Helsinki-NLP/opus-mt-en-pt'
        self.model_pt_en_name = 'Helsinki-NLP/opus-mt-pt-en'

        self.tokenizer_en_pt = MarianTokenizer.from_pretrained(self.model_en_pt_name)
        self.model_en_pt = MarianMTModel.from_pretrained(self.model_en_pt_name)

        self.tokenizer_pt_en = MarianTokenizer.from_pretrained(self.model_pt_en_name)
        self.model_pt_en = MarianMTModel.from_pretrained(self.model_pt_en_name)
        print("Modelos carregados com sucesso!")

    def translate(self, text, direction):
        if not text.strip():
            return "Entrada vazia."

        lines = [line.strip() for line in text.split('\n') if line.strip()]

        if direction == "Inglês → Português":
            tokenizer, model = self.tokenizer_en_pt, self.model_en_pt
        elif direction == "Português → Inglês":
            tokenizer, model = self.tokenizer_pt_en, self.model_pt_en
        else:
            return "❌ Direção de tradução inválida."

        tokens = tokenizer(lines, return_tensors="pt", padding=True, truncation=True)
        output = model.generate(**tokens, max_length=512, num_beams=4, early_stopping=True)
        translated = tokenizer.batch_decode(output, skip_special_tokens=True)

        return '\n'.join(translated)
