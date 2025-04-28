from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

# Banco - Usuário e Senha - Rota - Porta - BD Inicial
# Melhor utilizar .ENV e injetar variável abaixo!
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@localhost:5432/postgres"

db.init_app(app)