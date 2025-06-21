from flask import Flask, render_template, request, jsonify
from produtos_utils import carregar_produtos, salvar_produtos
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ======== ROTAS DE PÁGINAS ========

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vidros')
def vidros():
    return render_template('vidros.html')

@app.route('/essenciaambiente')
def essenciaambiente():
    return render_template('essenciaambiente.html')

@app.route('/produtos', methods=["GET"])
def listar():
    return jsonify(carregar_produtos())

@app.route('/produtos', methods=["POST"])
def adicionar():
    produtos = carregar_produtos()
    novo = request.json
    novo["id"] = produtos[-1]["id"] + 1 if produtos else 1
    produtos.append(novo)
    salvar_produtos(produtos)
    return jsonify({"Mensagem":"Produto adicionado com sucesso!"})

@app.route("/produtos/<int:id>", methods=["PUT"])
def editar(id):
    produtos = carregar_produtos()
    dados = request.json
    for produto in produtos:
        if produto["id"] == id:
            produto["nome"] = dados["nome"]
            produto["quantidade"] = dados["quantidade"]
            produto["preco"] = dados["preco"]
            break
    salvar_produtos(produtos)
    return jsonify({"mensagem": "Produto atualizado com sucesso"})

@app.route("/produtos/<int:id>", methods=["DELETE"])
def excluir(id):
    produtos = carregar_produtos()
    produtos = [p for p in produtos if p["id"] != id]
    salvar_produtos(produtos)
    return jsonify({"mensagem": "Produto excluído com sucesso"})

@app.route('/essenciaperfume')
def essenciaperfume():
    return render_template('essenciaperfume.html')

@app.route('/outros')
def outros():
    return render_template('outros.html')




if __name__ == '__main__':
    app.run(debug=True)
