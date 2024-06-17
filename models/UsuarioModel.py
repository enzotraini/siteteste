from main import db


class Usuario(db.Model):

    __tablename__ = 'Usuario'

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(45))
    email = db.Column(db.String(45))
    senha = db.Column(db.String(200))
    setor_id = db.Column(db.Integer, db.ForeignKey("Setor.id"))

    def serialize(self):
        return {
            'id': self.id,
            'usuario': self.usuario,
            'email': self.email
        }

  

