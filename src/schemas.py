from src.database.models import Film, Actor
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class FilmSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        exclude = ('id',)
        load_instance = True

class ActorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Actor
        load_instance = True