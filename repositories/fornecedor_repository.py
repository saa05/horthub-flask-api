from models import db, Fornecedor


def get_all_fornecedores():
    return Fornecedor.query.all()


def get_fornecedor_by_cnpj(cnpj):
    return Fornecedor.query.get(cnpj)


def create_fornecedor(cnpj, nome, telefone, email, endereco, certificacaoSAT):
    fornecedor = Fornecedor(cnpj=cnpj, nome=nome, telefone=telefone, email=email, endereco=endereco,
                            certificacaoSAT=certificacaoSAT)
    db.session.add(fornecedor)
    db.session.commit()
    return fornecedor


def update_fornecedor(fornecedor, nome, telefone, email, endereco, certificacaoSAT):
    fornecedor.nome = nome
    fornecedor.telefone = telefone
    fornecedor.email = email
    fornecedor.endereco = endereco
    fornecedor.certificacaoSAT = certificacaoSAT
    db.session.commit()
    return fornecedor


def delete_fornecedor(fornecedor):
    db.session.delete(fornecedor)
    db.session.commit()
