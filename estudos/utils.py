from functools import wraps
from flask import session, redirect, url_for, flash
from pathlib import Path

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            flash("Você precisa estar logado para acessar esta página.", "warning")
            return redirect(url_for('views.login'))  # redireciona para a rota de login
        return f(*args, **kwargs)
    return decorated_function