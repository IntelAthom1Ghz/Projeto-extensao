from flask import Blueprint, render_template, request, redirect,url_for, session
import sqlite3
import hashlib

views = Blueprint('views', __name__)

#redireciona a pessoa que acesssar a raiz do site, direto pro login
@views.route('/')
def index():
    return redirect(url_for('views.login')) #redireciono o usuario para o views.login
def gerar_hash(senha):
        return hashlib.sha256(senha.encode()).hexdigest()
@views.route('/login', methods =['GET', 'POST'])
def login():
    erro = None
    if request.method =='POST':
        email = request.form['email']
        senha = request.form['senha']
        senha_hash = gerar_hash(senha)
        with sqlite3.connect('app/usuarios.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE email = ? and SENHA = ?', (email, senha_hash))
            usuario = cursor.fetchone()

            if usuario:
                session['usuario'] = usuario[1] #nome guardado na session
                return redirect(url_for('views.dashboard')) #login sbem sucedido, manda pra dashboard do site
            else:
                erro ='Login Inválido'
    return render_template('login.html', erro=erro)
            
@views.route('/cadastro', methods =['GET','POST'])
def cadastro():
    erro = None

    if request.method =='POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        senha_hash = gerar_hash(senha)

        with sqlite3.connect('app/usuarios.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?,?,?)', (nome, email, senha_hash))
                conn.commit()
                return redirect(url_for('views.login'))
            except sqlite3.IntegrityError:
                erro = 'Email já cadastrado'
    return render_template('cadastro.html', erro = erro)

@views.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return render_template('dashboard.html', nome = session['usuario'])
    return redirect(url_for('views.login'))
@views.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('views.login'))
    