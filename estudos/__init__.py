from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    app.secret_key ='chave_super_secreta'

    #banco de dados aqui
    from .database import init_db
    init_db()

    #importar e registrar as rotas do app
    from .views import views
    app.register_blueprint(views)

    return app