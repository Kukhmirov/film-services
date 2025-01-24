from flask_restful import Resource

from src.resources.auth import token_required
from src.schemas.actors import ActorSchema

class ActorListApi(Resource):
    actor_schema = ActorSchema()

    @token_required
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def patch(self):
        pass
    def delete(self):
        pass