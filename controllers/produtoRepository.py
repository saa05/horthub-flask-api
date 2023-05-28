from flask_restful import reqparse, Resource
from flask_apispec import marshal_with, use_kwargs, doc
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields, post_dump

from repositories.produto_repository import (
    get_all_produtos,
    get_produto_by_id,
    create_produto,
    update_produto,
    delete_produto
)


class ProdutoResponseSchema(Schema):
    id = fields.Integer(required=True)
    nome = fields.Str(required=True)
    cor = fields.Str(required=True)
    peso = fields.Float(required=True)
    preco = fields.Float(required=True)
    quantidade = fields.Integer(required=True)
    tipo = fields.Str(required=True)

    @post_dump(pass_many=True)
    def wrap_with_data_key(self, data, many, **kwargs):
        return {'data': data}


class ProdutoReqSchema(Schema):
    nome = fields.Str(required=True)
    cor = fields.Str(required=True)
    peso = fields.Float(required=True)
    preco = fields.Float(required=True)
    quantidade = fields.Integer(required=True)
    tipo = fields.Str(required=True)


class ProdutoController(MethodResource, Resource):
    @doc(description='Obter produto pelo ID', tags=['Produtos'])
    @marshal_with(ProdutoResponseSchema)
    def get(self, id):
        produto = get_produto_by_id(id)
        if produto:
            return produto, 200
        return {'message': 'Produto not found'}, 404

    @doc(description='Atualizar produto pelo ID', tags=['Produtos'])
    @marshal_with(ProdutoResponseSchema)
    @use_kwargs(ProdutoReqSchema, location=('json'), apply=None)
    def put(self, id, **kwargs):

        produto = get_produto_by_id(id)
        if produto:
            produto = update_produto(
                produto,
                **kwargs,
            )
            return produto, 200
        return {'message': 'Produto not found'}, 404

    @doc(description='Excluir produto pelo ID', tags=['Produtos'])
    def delete(self, id):
        produto = get_produto_by_id(id)
        if produto:
            delete_produto(produto)
            return {'message': 'Produto deleted'}, 200
        return {'message': 'Produto not found'}, 404


class ProdutoListController(MethodResource, Resource):
    @doc(description='Obter todos os produtos', tags=['Produtos'])
    @marshal_with(ProdutoResponseSchema(many=True))
    def get(self):
        produtos = get_all_produtos()
        return produtos, 200

    @doc(description='Criar um novo produto', tags=['Produtos'])
    @marshal_with(ProdutoResponseSchema)
    @use_kwargs(ProdutoReqSchema, location='json')
    def post(self, **kwargs):
        produto = create_produto(
            **kwargs
        )

        return produto, 201
