
from flask import Flask, render_template_string, request, send_file
from docxtpl import DocxTemplate
import os
import datetime

app = Flask(__name__)

# Carregar o formulário HTML direto de string
with open("formulario_certificado_itbi_condicional.html", "r", encoding="utf-8") as f:
    html_form = f.read()

@app.route("/")
def index():
    return render_template_string(html_form)

@app.route("/gerar", methods=["POST"])
def gerar_documento():
    # Coletar os dados do formulário
    dados = {chave: request.form[chave] for chave in request.form}

    # Carregar o modelo Word
    doc = DocxTemplate("modelo_certificado_itbi_condicional.docx")
    doc.render(dados)

    # Nome do arquivo final
    nome_arquivo = f"certificado_itbi_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.docx"
    caminho_saida = os.path.join("output", nome_arquivo)

    # Criar pasta output se não existir
    os.makedirs("output", exist_ok=True)

    # Salvar o documento
    doc.save(caminho_saida)

    return send_file(caminho_saida, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
