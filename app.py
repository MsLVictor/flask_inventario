import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

database_url = os.environ.get('DATABASE_URL')

# Ajuste para Render: troca 'postgres://' por 'postgresql://'
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url

# Desabilita o rastreamento de modificações, o que economiza memória
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy com o aplicativo Flask
db = SQLAlchemy(app)

# --- Modelo Produto ---
# Define o modelo de dados para a tabela 'Produto' no banco de dados
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Produto('{self.nome}', Quantidade: {self.quantidade}, Preco: {self.preco})"

    # Método para converter o objeto Produto em um dicionário (útil para JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco
        }

# Cria as tabelas no banco de dados se elas não existirem
# Isso deve ser feito dentro do contexto da aplicação
with app.app_context():
    db.create_all()

# ======== ROTAS DE PÁGINAS ========
# As rotas de renderização de templates permanecem as mesmas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vidros')
def vidros():
    return render_template('vidros.html')

@app.route('/essenciaambiente')
def essenciaambiente():
    return render_template('essenciaambiente.html')

#nova rota para pesquisa assincrona
@app.route('/search_essencia')
def search_essencia():
    query = request.args.get('q', '').strip()
    # Se a query estiver vazia, retorne todas as essências (ou decida seu comportamento)
    if not query:
        produtos = Produto.query.order_by(Produto.nome).all()
    else:
        # Consulta ao banco de dados filtrando pelo termo de pesquisa
        produtos = Produto.query.filter(
            Produto.nome.ilike(f'%{query}%')).all()
    # Converte os objetos Essencia em uma lista de dicionários
    produtos_data = [p.to_dict() for p in produtos]

    # Retorna os dados como JSON
    return jsonify(produtos=produtos_data)

@app.route('/essenciaperfume')
def essenciaperfume():
    return render_template('essenciaperfume.html')

@app.route('/outros')
def outros():
    return render_template('outros.html')

# ======== ROTAS DE PRODUTOS (CRUD) ========
@app.route('/produtos', methods=["GET"])
def listar():
    produtos = Produto.query.order_by(Produto.nome).all()
    return jsonify([p.to_dict() for p in produtos])

@app.route('/produtos', methods=["POST"])
def adicionar():
    data = request.get_json()
    novo = Produto(
        nome=data["nome"],
        quantidade=data["quantidade"],
        preco=data["preco"]
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify(novo.to_dict()), 201

@app.route("/produtos/<int:id>", methods=["PUT"])
def editar(id):
    produto = Produto.query.get_or_404(id)
    data = request.get_json()
    produto.nome = data["nome"]
    produto.quantidade = data["quantidade"]
    produto.preco = data["preco"]
    db.session.commit()
    return jsonify(produto.to_dict())

@app.route("/produtos/<int:id>", methods=["DELETE"])
def excluir(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return jsonify({"mensagem": "Produto excluído com sucesso"})



# Executa o aplicativo em modo de depuração se o script for o principal
if __name__ == '__main__':
    app.run(debug=True)