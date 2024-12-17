from src.database.models import Actor
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ActorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Actor
        load_instance = True