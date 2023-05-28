from flask_restful import reqparse, Resource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields, post_dump
from repositories.fornecedor_repository import (
    get_all_fornecedores,
    get_fornecedor_by_cnpj,
    create_fornecedor,
    update_fornecedor,
    delete_fornecedor
)


class FornecedorResponseSchema(Schema):
    cnpj = fields.Str(required=True)
    nome = fields.Str(required=True)
    telefone = fields.Str(required=True)
    email = fields.Str(required=True)
    endereco = fields.Str(required=True)
    certificacaoSAT = fields.Str(required=True)

    @post_dump(pass_many=True)
    def wrap_with_data_key(self, data, many, **kwargs):
        return {'data': data}


class FornecedorReqSchema(Schema):
    cnpj = fields.Str(required=True)
    nome = fields.Str(required=True)
    telefone = fields.Str(required=True)
    email = fields.Str(required=True)
    endereco = fields.Str(required=True)
    certificacaoSAT = fields.Str(required=True)


class FornecedorController(MethodResource, Resource):
    @doc(description='Busca fornecedor pelo CNPJ', tags=['Fornecedores'])
    @marshal_with(FornecedorResponseSchema)
    def get(self, cnpj):
        fornecedor = get_fornecedor_by_cnpj(cnpj)
        if fornecedor:
            return fornecedor, 200
        return {'message': 'Fornecedor not found'}, 404

    @doc(description='Atualizar fornecedor pelo CNPJ', tags=['Fornecedores'])
    @marshal_with(FornecedorResponseSchema)
    @use_kwargs(FornecedorReqSchema, location=('json'), apply=None)
    def put(self, cnpj, **kwargs):

        fornecedor = get_fornecedor_by_cnpj(cnpj)
        if fornecedor:
            fornecedor = update_fornecedor(fornecedor, **kwargs)
            return fornecedor, 200
        return {'message': 'Fornecedor not found'}, 404

    @doc(description='Excluir fornecedor pelo CNPJ', tags=['Fornecedores'])
    def delete(self, cnpj):
        fornecedor = get_fornecedor_by_cnpj(cnpj)
        if fornecedor:
            delete_fornecedor(fornecedor)
            return {'message': 'Fornecedor deleted'}, 200
        return {'message': 'Fornecedor not found'}, 404


class FornecedorListController(MethodResource, Resource):
    @doc(description='Obter todos os fornecedores', tags=['Fornecedores'])
    @marshal_with(FornecedorResponseSchema(many=True))
    def get(self):
        fornecedores = get_all_fornecedores()
        return fornecedores, 200

    @doc(description='Criar um novo fornecedor', tags=['Fornecedores'])
    @marshal_with(FornecedorResponseSchema)
    @use_kwargs(FornecedorReqSchema, location=('json'), apply=None)
    def post(self, **kwargs):
        fornecedor = create_fornecedor(**kwargs)
        return fornecedor, 201
