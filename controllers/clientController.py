from flask_restful import reqparse, Resource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields, post_dump

from repositories.cliente_repository import (
    get_all_Clientes,
    get_Cliente_by_cpf,
    create_Cliente,
    update_Cliente,
    delete_Cliente
)


class ClienteResponseSchema(Schema):
    cpf = fields.Str(required=True)
    nome = fields.Str(required=True)
    telefone = fields.Str(required=True)
    email = fields.Str(required=True)
    endereco = fields.Str(required=True)

    @post_dump(pass_many=True)
    def wrap_with_data_key(self, data, many, **kwargs):
        return {'data': data}


class ClienteController(MethodResource, Resource):
    @doc(description='Obter cliente pelo CPF', tags=['Clientes'])
    @marshal_with(ClienteResponseSchema)
    def get(self, cpf):
        cliente = get_Cliente_by_cpf(cpf)
        if cliente:
            return cliente, 200
        return {'message': 'Cliente not found'}, 404

    @doc(description='Atualiza um cliente pelo CPF', tags=['Clientes'])
    @marshal_with(ClienteResponseSchema)
    @use_kwargs(ClienteResponseSchema, location=('json'), apply=None)
    def put(self, cpf, **kwargs):

        cliente = get_Cliente_by_cpf(cpf)
        if cliente:
            update_Cliente(cliente, **kwargs)
            return cliente, 200
        return {'message': 'Cliente not found'}, 404

    @doc(description='Deleta um cliente pelo CPF', tags=['Clientes'])
    def delete(self, cpf):
        cliente = get_Cliente_by_cpf(cpf)
        if cliente:
            delete_Cliente(cliente)
            return {'message': 'Cliente deleted'}, 200
        return {'message': 'Cliente not found'}, 404


class ClienteListController(MethodResource, Resource):
    @doc(description='Obter todos clientes', tags=['Clientes'])
    @marshal_with(ClienteResponseSchema(many=True))
    def get(self):
        clientes = get_all_Clientes()
        return clientes, 200

    @doc(description='Cria um novo cliente', tags=['Clientes'])
    @marshal_with(ClienteResponseSchema)
    @use_kwargs(ClienteResponseSchema, location=('json'), apply=None)
    def post(self, **kwargs):
        cliente = create_Cliente(**kwargs)

        return cliente, 201
