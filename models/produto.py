from models import db


class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cor = db.Column(db.String(50))
    peso = db.Column(db.Float)
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    tipo = db.Column(db.String(50))
    def __init__(self, nome, cor, peso, preco, quantidade, tipo):
        self.nome = nome
        self.cor = cor
        self.peso = peso
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo

    def to_dict(self):
        return {
            'id': self.id,
             'nome': self.nome,
             'cor': self.cor,
            'peso': self.peso,
            'preco': self.preco,
         'quantidade': self.quantidade,
         'tipo': self.tipo
            }

    def __iter__(self):
        return self.to_dict().items()
