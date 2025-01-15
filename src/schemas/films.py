from marshmallow_sqlalchemy.fields import Nested

from src.database.models import Film
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class FilmSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        exclude = ('id',)
        load_instance = True
        include_fk = True
    actors = Nested('ActorSchema', many=True, exclude=('films',))