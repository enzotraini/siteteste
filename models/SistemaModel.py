from main import db


class Sistema(db.Model):

    __tablename__ = 'Setor'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45))
    email =db.Column(db.String(45))


    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
        }