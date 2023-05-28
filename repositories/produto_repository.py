from models import db, Produto


def get_all_produtos():
    return Produto.query.all()


def get_produto_by_id(id):
    return Produto.query.get(id)


def create_produto(nome, cor, peso, preco, quantidade, tipo):
    produto = Produto(nome=nome, cor=cor, peso=peso, preco=preco, quantidade=quantidade, tipo=tipo)
    db.session.add(produto)
    db.session.commit()
    return produto


def update_produto(produto, nome, cor, peso, preco, quantidade, tipo):
    produto.nome = nome
    produto.cor = cor
    produto.peso = peso
    produto.preco = preco
    produto.quantidade = quantidade
    produto.tipo = tipo
    db.session.commit()
    return produto


def delete_produto(produto):
    db.session.delete(produto)
    db.session.commit()
