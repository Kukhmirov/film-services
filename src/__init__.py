import config

from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)

SWAGGER_URL = '/documentation'
APPI_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    APPI_URL,
    config={
        'app_name': 'Films API',
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

from . import routes, models