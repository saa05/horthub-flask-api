from flask_restful import Api

api = Api()

from .clientController import ClienteController, ClienteListController
from .fornecedorController import FornecedorController, FornecedorListController
from .produtoRepository import ProdutoController, ProdutoListController

api.add_resource(ClienteListController, '/clientes')
api.add_resource(ClienteController, '/clientes/<string:cpf>')

api.add_resource(FornecedorListController, '/fornecedores')
api.add_resource(FornecedorController, '/fornecedores/<string:cnpj>')


api.add_resource(ProdutoListController, '/produtos')
api.add_resource(ProdutoController, '/produtos/<int:id>')
