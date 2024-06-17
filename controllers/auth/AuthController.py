from main import app, db, bcrypt
from flask import render_template, request, session, url_for, redirect
from models.UsuarioModel import Usuario
from models.SetorModel import Setor
from flask_bcrypt import generate_password_hash

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template('auth/login.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        usuario = request.form['usuario']
        setor_id = int(request.form['setor'])  
        email = request.form['email']
        senha = bcrypt.generate_password_hash(request.form['senha']).decode('utf-8')

        novo_usuario = Usuario(usuario=usuario, setor_id=setor_id, email=email, senha=senha)

        db.session.add(novo_usuario)
        db.session.commit()


        return redirect(url_for('login'))
    
    return render_template('auth/cadastrar.html')


@app.route('/esqueci_senha', methods=['GET'])
def esqueci_senha():
    return render_template('auth/esqueceu.html')
