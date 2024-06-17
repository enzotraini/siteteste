import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY') 

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario=os.getenv('USUARIO'),
        senha=os.getenv('PASSWORD'),
        servidor=os.getenv('SERVER'),
        database=os.getenv('DATABASE')
    )