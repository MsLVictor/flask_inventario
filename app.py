import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# --- Configuração do Banco de Dados ---
# Tenta obter a URI do banco de dados de uma variável de ambiente (ideal para produção/nuvem)
# Se não estiver definida, usa uma URI de exemplo para PostgreSQL local (para desenvolvimento)
# Formato da URI para PostgreSQL: postgresql://user:password@host:port/database_name
# Ex: 'postgresql://postgres:mysecretpassword@localhost:5432/meu_inventario_db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

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

@app.route('/essenciaperfume')
def essenciaperfume():
    return render_template('essenciaperfume.html')

@app.route('/outros')
def outros():
    return render_template('outros.html')

# ======== ROTAS DE PRODUTOS (CRUD) ========
# As rotas da API CRUD para produtos permanecem as mesmas,
# pois o SQLAlchemy abstrai o banco de dados subjacente
@app.route('/produtos', methods=["GET"])
def listar():
    produtos = Produto.query.all()
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
