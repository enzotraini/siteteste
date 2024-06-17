from main import app, db
from flask import render_template, request, redirect, url_for, session
from models.UsuarioModel import Usuario
from flask_bcrypt import bcrypt


@app.route('/entrar', methods=['POST', 'GET'])
def entrar():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not email or not senha:
            return "Email ou senha não fornecidos", 400

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and bcrypt.check_password_hash(usuario.senha, senha):
            session['usuario_email'] = usuario.email
            session['usuario_senha'] = usuario.senha
            return redirect(url_for('sistema')) 
        else:
            return "Usuário ou senha inválidos", 401
    
    return render_template('auth/login.html')


@app.route('/sistema')
def sistema():
    return render_template('sistema.html')

 