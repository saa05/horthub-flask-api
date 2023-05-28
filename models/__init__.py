from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .cliente import Cliente
from .produto import Produto
from .fornecedor import Fornecedor