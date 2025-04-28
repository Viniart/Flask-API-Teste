docker run --name postgres-db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres -- Inicialização de contâiner com o PostgreSQL

virtual\Scripts\activate -- Ativar o ambiente virtual Python para instalação de dependências

pip install Flask Flask-SQLAlchemy PYJWT -- Flask, ORM (SQL Alchemy) e PYJWT para trabalhar com tokens
pip install psycopg2-binary -- Adaptador do Python para PostgreSQL

flask shell -- Terminal do Flask

db.create_all() 