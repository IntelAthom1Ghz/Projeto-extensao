from flask import Flask
import os
from flask_bcrypt import Bcrypt
from datetime import timedelta
import secrets
from dotenv import load_dotenv

bcrypt = Bcrypt()
def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.secret_key = os.environ.get('SECRET_KEY') or secrets.token_hex(64)

    app.permanent_session_lifetime = timedelta(minutes=15)
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SECURE'] = True #https
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

    #banco de dados aqui
    from .database import init_db
    init_db()
    bcrypt.init_app(app)

    #importar e registrar as rotas do app
    from .views import views
    app.register_blueprint(views)

    return app