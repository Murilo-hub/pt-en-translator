import gradio as gr
from app.translator import Translator

translator = Translator()

def translate_interface(text, direction):
    return translator.translate(text, direction)

def clear_fields():
    return "", ""

def launch_interface():
    with gr.Blocks() as app:
        gr.Markdown("# 🌍 Tradutor EN ↔ PT")
        gr.Markdown("Escolha a direção da tradução, insira o texto e clique em traduzir!")

        with gr.Row():
            input_text = gr.Textbox(label="Texto original", lines=6, placeholder="Digite aqui...")
            output_text = gr.Textbox(label="Tradução", lines=6)

        direction = gr.Radio(
            choices=["Inglês → Português", "Português → Inglês"],
            label="Direção da tradução",
            value="Inglês → Português"
        )

        with gr.Row():
            translate_btn = gr.Button("🔁 Traduzir")
            clear_btn = gr.Button("🧹 Limpar")

        translate_btn.click(fn=translate_interface, inputs=[input_text, direction], outputs=output_text)
        clear_btn.click(fn=clear_fields, outputs=[input_text, output_text])

    app.launch(share=True)
