from flask import request

from flask_restful import Resource
from sqlalchemy.orm import joinedload

from src import db
from src.database.models import Film, Actor

from marshmallow import ValidationError

from src.database.queries import start
from src.database.seed_mok_db import seed_database
from src.schemas.films import FilmSchema


class FilmListApi(Resource):
    film_schema = FilmSchema()

    def get(self, uuid=None):
        seed_database()
        if not uuid:
            films = db.session.query(Film).options(
                joinedload(Film.actors)
            ).all()
            films_dict = self.film_schema.dump(films, many=True)
            start()
            return films_dict
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return '', 404
        return self.film_schema.dump(film)

    def post(self):
        try:
            print(request.json)
            film = self.film_schema.load(request.json, session=db.session)
            print(film)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 201

    def put(self, uuid):
        # Без использования схемы marshmallow
        # film_json = request.get_json()
        # if not film_json:
        #     return {"message": "Нет обьекта"}, 400
        # try:
        #     db.session.query(Film).filter_by(uuid=uuid).update(
        #         dict(
        #             title=film_json['title'],
        #             release_date=datetime.strptime(film_json['release_date'], '%Y-%m-%d'),
        #             description=film_json.get('description', ''),
        #             rating=film_json.get('rating', ''),
        #             distributed_by=film_json.get('distributed_by', ''),
        #             film_length=film_json.get('film_length', ''),
        #         )
        #     )
        #     db.session.commit()
        #     print(db.session.query(Film).all())
        #     film = db.session.query(Film).filter_by(uuid=uuid).first()
        #     return jsonify(film.to_dict())
        # except (ValueError, KeyError) as e:
        #     return {"message": "Не удалось изменить обьект"}, 400

        film = Film.query.filter_by(uuid=uuid).first()
        if not film:
            return 'Фильм не найден', 404
        try:
            film = self.film_schema.load(request.get_json(), instance=film, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 200

    def patch(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return {"message": "Нет такого фильма"}, 404
        try:
            film_json = request.get_json(silent=True)
            if not film_json:
                return {'message': 'Request body is missing or not in JSON format'}, 400
            updated_film = self.film_schema.load(film_json, instance=film, session=db.session, partial=True)
        except ValidationError as e:
            return {'message': e.messages}, 400

        db.session.commit()
        return self.film_schema.dump(updated_film), 200

    def delete(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return {"message", "Такого фильма нет в БД"}, 404
        db.session.delete(film)
        db.session.commit()
        return {"message": "Фильм удален"}, 200