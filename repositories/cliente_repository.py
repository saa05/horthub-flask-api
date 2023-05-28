from models import db, Cliente


def get_all_Clientes():
    return Cliente.query.all()

def get_Cliente_by_cpf(cpf):
    return Cliente.query.get(cpf)


def create_Cliente(cpf, nome, telefone, email, endereco):
    cliente = Cliente(cpf=cpf, nome=nome, telefone=telefone, email=email, endereco=endereco)
    db.session.add(cliente)
    db.session.commit()
    return Cliente


def update_Cliente(Cliente, nome, telefone, email, endereco):
    Cliente.nome = nome
    Cliente.telefone = telefone
    Cliente.email = email
    Cliente.endereco = endereco
    db.session.commit()
    return Cliente


def delete_Cliente(Cliente):
    db.session.delete(Cliente)
    db.session.commit()
