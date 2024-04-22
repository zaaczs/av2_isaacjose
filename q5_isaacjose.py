#flask gera hashes de senha criptografados.
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__, template_folder='arquivos')

bcrypt = Bcrypt(app)
app.secret_key = os.urandom(24)

# Dicionário de usuários
users = {
    "usuario1": {"id": "usuario1", "nome": "João", "email": "joao@email.com", "endereco": "Rua A, 123", "senha": bcrypt.generate_password_hash("senha123").decode('utf-8')},
    "usuario2": {"id": "usuario2", "nome": "Maria", "email": "maria@email.com", "endereco": "Rua B, 456", "senha": bcrypt.generate_password_hash("senha456").decode('utf-8')},
    "usuario3": {"id": "usuario3", "nome": "Carlos", "email": "carlos@email.com", "endereco": "Rua C, 789", "senha": bcrypt.generate_password_hash("senha789").decode('utf-8')}
}

# Rotas
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']

        user = users.get(user_id)
        if user and bcrypt.check_password_hash(user['senha'], password):
            session['user_id'] = user['id']
            return redirect(url_for('dashboard'))

        return render_template('login.html', message='Credenciais inválidas!')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user_id = session['user_id']
        user = users.get(user_id)
        return render_template('dashboard.html', user=user)

    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
