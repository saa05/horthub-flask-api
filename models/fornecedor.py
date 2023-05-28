from models import db
class Fornecedor(db.Model):
    __tablename__ = 'fornecedores'
    cnpj = db.Column(db.String(14), primary_key=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    endereco = db.Column(db.String(200))
    certificacaoSAT = db.Column(db.String(100))

    def to_dict(self):
        return {
            'cnpj': self.cnpj,
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
            'endereco': self.endereco,
            'certificacaoSAT': self.certificacaoSAT
        }

    def __iter__(self):
        return self.to_dict().items()
