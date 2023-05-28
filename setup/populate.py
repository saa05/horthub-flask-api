from flask_sqlalchemy import SQLAlchemy

from models.cliente import Cliente
from models.fornecedor import Fornecedor
from models.produto import Produto
from repositories.cliente_repository import get_all_Clientes


def populate_data(db: SQLAlchemy):
    # caso ja populado sai do codigo
    if len(get_all_Clientes()) > 0:
        return
    # Popula um exemplo de cliente
    endereco = "Rua Estevão Fernandes, 123 - João dias - São Paulo - SP"
    Cliente1 = Cliente(cpf='12345678901', nome='João da Silva', telefone='123456789',
                         email='joao.silva@gamil.com',
                         endereco=endereco)

    db.session.add(Cliente1)

    # Popula alguns exemplos de produtos
    produto1 = Produto("Maçã", "vermelha", 0.5, 2.50, 10, "fruta")
    produto2 = Produto("Tomate", "vermelho", 1.0, 4.00, 5, "legume")
    produto3 = Produto("Alface", "verde", 0.2, 2.00, 20, "verdura")
    produto4 = Produto("Mel", "dourado", 0.3, 20.00, 2, "produto apícola")

    db.session.add(produto1)
    db.session.add(produto2)
    db.session.add(produto3)
    db.session.add(produto4)

    # Popula um exemplo de fornecedor
    endereco_fornecedor = "av Santo Amaro,123 - Santo Amaro - São Paulo - SP"
    fornecedor1 = Fornecedor(cnpj='12345678901234', nome='João da Silva', telefone='123456789',
                             email='joao.silva@gamil.com', endereco=endereco_fornecedor,
                             certificacaoSAT='555283034')
    db.session.add(fornecedor1)

    db.session.commit()
