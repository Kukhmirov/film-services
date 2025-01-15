from marshmallow_sqlalchemy.fields import Nested

from src.database.models import Actor
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class ActorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Actor
        load_instance = True
        include_fk = True
    films = Nested('ActorSchema', many=True, exclude=('films',))