# Flask Inventário

Sistema simples de controle de inventário desenvolvido com Flask e banco de dados PostgreSQL. Permite gerenciar produtos em várias categorias, com funcionalidades básicas de CRUD (Criar, Ler, Atualizar e Deletar).

---

## Índice

* [Descrição](#descrição)
* [Funcionalidades](#funcionalidades)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Configuração e Execução](#configuração-e-execução)
* [API Endpoints](#api-endpoints)
* [Contribuição](#contribuição)
* [Licença](#licença)

---

## Descrição

Este projeto é uma aplicação web para controle de inventário, construída com Flask (Python), utilizando SQLAlchemy para manipulação do banco de dados PostgreSQL. Oferece uma interface web para cadastro e gerenciamento de produtos, organizados em diferentes categorias como vidros, essências para ambiente, essências para perfume e outros.

---

## Funcionalidades

* Cadastro de produtos com nome, quantidade e preço.
* Listagem de produtos.
* Edição de informações dos produtos.
* Exclusão de produtos.
* Páginas específicas para categorias de produtos (vidros, essências, outros).
* Uso de banco de dados PostgreSQL para persistência dos dados.
* API REST para integração e consumo dos dados via JSON.

---

## Tecnologias Utilizadas

* Python 3.x
* Flask
* Flask-SQLAlchemy
* PostgreSQL
* psycopg2 (driver PostgreSQL para Python)
* python-dotenv (para carregar variáveis de ambiente)
* HTML/CSS para templates

---

## Estrutura do Projeto

```
flask_inventario/
|
|├── app.py                  # Aplicação principal Flask
|├── requirements.txt        # Dependências do projeto
|├── .env                    # Variáveis de ambiente (não versionado)
|├── templates/              # Arquivos HTML para renderização das páginas
|   |├── index.html
|   |├── vidros.html
|   |├── essenciaambiente.html
|   |├── essenciaperfume.html
|   |└── outros.html
|├── static/                 # Arquivos estáticos (CSS, JS, imagens)
└── README.md               # Documentação do projeto
```

---

## Configuração e Execução

1. **Clone o repositório:**

```bash
git clone https://github.com/MsLVictor/flask_inventario.git
cd flask_inventario
```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/macOS
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente:**

Crie um arquivo `.env` na raiz do projeto com a variável do banco de dados, por exemplo:

```
DATABASE_URL=postgresql://usuario:senha@endereco:porta/nome_do_banco
```

5. **Execute a aplicação:**

```bash
python app.py
```

Acesse no navegador em [http://localhost:5000](http://localhost:5000).

---

## API Endpoints

| Método | URL              | Descrição                 |
| ------ | ---------------- | ------------------------- |
| GET    | `/produtos`      | Lista todos os produtos   |
| POST   | `/produtos`      | Adiciona um novo produto  |
| PUT    | `/produtos/<id>` | Edita um produto pelo ID  |
| DELETE | `/produtos/<id>` | Exclui um produto pelo ID |

**Exemplo JSON para POST/PUT:**

```json
{
  "nome": "Produto Exemplo",
  "quantidade": 10,
  "preco": 25.5
}
```

---

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto.
2. Crie uma branch com a sua feature: `git checkout -b minha-feature`.
3. Faça commit das suas alterações: `git commit -m "Minha feature"`.
4. Envie para o repositório remoto: `git push origin minha-feature`.
5. Abra um Pull Request.

---

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.
