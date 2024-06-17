from main import db


class Setor(db.Model):

    __tablename__ = 'Setor'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45))


    def serialize(self):
        return {
            'id': self.id,
            '1': self.Diretoria,
            '2':self.Producao,
            '3':self.Experiencia,
            '4':self.Financeiro,
            '5':self.Administrativo,
            '6':self.Vendas,
            '7':self.Gerencia, 
        }
