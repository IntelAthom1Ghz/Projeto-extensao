from flask import Flask

def criar_app():
    app = Flask(__name__)

    from .views import views
    app.register_blueprint(views)

    return app
