from datetime import datetime
from flask import request, Response, jsonify

from flask_restful import Resource
from src import api, db
from src.models import Film


class Smoke(Resource):
    def get(self):
        return {'mesage': 'ok'}, 200

class FilmListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            films = db.session.query(Film).all()
            films_dict = [f.to_dict() for f in films]
            return jsonify(films_dict)
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return '', 404
        return jsonify(film.to_dict())

    def post(self):
        film_json = request.get_json()
        if not film_json:
            return {"message": "Нет обьекта"}, 400
        try:
            film = Film(
                title=film_json['title'],
                release_date=datetime.strptime(film_json['release_date'], '%Y-%m-%d'),
                distributed_by=film_json['distributed_by'],
                description=film_json.get('description', ''),
                film_length=film_json.get('film_length', ''),
                rating=film_json.get('rating', ''),
            )
            db.session.add(film)
            db.session.commit()
        except (ValueError, KeyError) as e:
            return {"message": "Не правильные данные"}, 400
        return {'message': 'Фильм создан'}, 201

    def put(self, uuid):
        film_json = request.get_json()
        if not film_json:
            return {"message": "Нет обьекта"}, 400
        try:
            db.session.query(Film).filter_by(uuid=uuid).update(
                dict(
                    title=film_json['title'],
                    release_date=datetime.strptime(film_json['release_date'], '%Y-%m-%d'),
                    description=film_json.get('description', ''),
                    rating=film_json.get('rating', ''),
                    distributed_by=film_json.get('distributed_by', ''),
                    film_length=film_json.get('film_length', ''),
                )
            )
            db.session.commit()
            print(db.session.query(Film).all())
            film = db.session.query(Film).filter_by(uuid=uuid).first()
            return jsonify(film.to_dict())
        except (ValueError, KeyError) as e:
            return {"message": "Не удалось изменить обьект"}, 400

    def patch(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return {"message": "Нет такого фильма"}, 404

        film_json = request.get_json()

        title = film_json.get('title')
        release_date = datetime.strptime(film_json.get('release_date'), '%Y-%m-%d') if film_json.get(
            'release_date') else None
        description = film_json.get('description', '')
        rating = film_json.get('rating', '')
        distributed_by = film_json.get('distributed_by', '')
        film_length = film_json.get('film_length', '')

        if title:
            film.title = title
        if release_date:
            film.release_date = release_date
        if description:
            film.description = description
        if rating:
            film.rating = rating
        if distributed_by:
            film.distributed_by = distributed_by
        if film_length:
            film.film_length = film_length

        db.session.commit()
        return film.to_dict(), 200

    def delete(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return {"message", "Такого фильма нет в БД"}, 404
        db.session.delete(film)
        db.session.commit()
        return {"message": "Фильм удален"}, 200

api.add_resource(Smoke, '/smoke')
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)