# Importa o Gradio (para interface web) e a classe Translator (criada)
import gradio as gr
from app.translator import Translator

# Instancia a classe Translator
translator = Translator()

def translate_interface(text, direction):
    return translator.translate(text, direction)

# Função de limpeza dos campos de texto
def limpar():
    return "", ""

def launch_interface():
    # Cria a interface gráfica com Gradio usando Blocks (layout personalizado)
    with gr.Blocks() as app:
        # Título e descrição
        gr.Markdown("# 🌍 Tradutor EN ↔ PT")
        gr.Markdown("Escolha a direção, digite seu texto e veja a tradução!")

        # Linha com caixas de texto lado a lado
        with gr.Row():
            entrada = gr.Textbox(label="Texto original", lines=6, placeholder="Digite aqui...")
            saida = gr.Textbox(label="Tradução", lines=6)

        # Escolha da direção da tradução
        direcao = gr.Radio(
            choices=["Inglês → Português", "Português → Inglês"],
            label="Direção da tradução",
            value="Inglês → Português"  # valor padrão
        )

        # Linha com botões
        with gr.Row():
            btn_traduzir = gr.Button("🔁 Traduzir")
            btn_limpar = gr.Button("🧹 Limpar")

        # Conecta o botão de traduzir à função translate da classe Translator
        btn_traduzir.click(
            fn=translator.translate,    # Função a ser chamada
            inputs=[entrada, direcao],  # Entradas vindas do usuário
            outputs=saida               # Saída para exibir a tradução
        )

        # Conecta o botão limpar à função limpar()
        btn_limpar.click(
            fn=limpar,
            outputs=[entrada, saida]
        )

    # Executa a aplicação com Gradio e permite compartilhamento público
    app.launch(share=True)
