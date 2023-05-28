from models import db
from marshmallow import Schema, fields


class Cliente(db.Model):
    __tablename__ = 'clientes'
    cpf = db.Column(db.String(11), primary_key=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    endereco = db.Column(db.String(200))

    def to_dict(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
            'endereco': self.endereco
        }

    def __iter__(self):
        return self.to_dict().items()
