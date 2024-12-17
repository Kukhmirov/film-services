from src.database.models import Film
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class FilmSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        exclude = ('id',)
        load_instance = True