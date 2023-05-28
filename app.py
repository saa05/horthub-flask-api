from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from setup.app_setup import create_app
from setup.env_cfg import setup_config
from models import *
from controllers import *
from setup.populate import populate_data

app = create_app()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = setup_config.sqlalchemy_track_notification
app.config['SQLALCHEMY_ECHO'] = setup_config.sqlalchemy_echo_enable
app.config['SQLALCHEMY_DATABASE_URI'] = setup_config.database_uri

api.init_app(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Projeto HortHub',
        version='alpha1.0.',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

docs.register(ClienteListController)
docs.register(ClienteController)
docs.register(FornecedorListController)
docs.register(FornecedorController)
docs.register(ProdutoListController)
docs.register(ProdutoController)

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        populate_data(db)
    app.run(debug=setup_config.debug_enable)
