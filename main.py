from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_pyfile('config.py')


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from controllers.IndexControll import *
from controllers.auth.AuthController import *
from controllers.SistemaController import *


if __name__ == '__main__':
    app.run(debug=True)
