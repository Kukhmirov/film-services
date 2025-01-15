"""
SELECT QUERIES
"""
from pprint import pprint

from src import db
from src.database import models

def start():
    films = db.session.query(models.Film).order_by(models.Film.rating.desc()).all()
    fight_club = db.session.query(models.Film).filter(models.Film.title == 'Fight Club').first()
    the_matrix = db.session.query(models.Film).filter(models.Film.title == 'The Matrix').first()
    lord_of_the_ring = db.session.query(models.Film).filter(
        models.Film.title != 'The Lord of the Rings: The Two Towers',
        models.Film.rating >= 8.5
    ).all()
    # like и ilike поиск с учетом регистра и без
    text_the = db.session.query(models.Film).filter(models.Film.release_date.like('%1994%')).all()

    # Поиск в диапозоне between, знак ~ = not . Поиск по точным значениям in_([...перечисление значений])
    sorted_by_length = db.session.query(models.Film).filter(~models.Film.film_length.between(150, 160))[:2]
    # pprint(sorted_by_length, width=50)

    """
    QUERYING WITH JOINS
    """
    films_with_actors = db.session.query(models.Film).join(models.Film.actors).all()
    actor_films = db.session.query(models.Actor).all()
    # for actor in actor_films:
    #     print(f"Актер: {actor.name}")
    #     if actor.films:  # Проверяем, есть ли фильмы
    #         for film in actor.films:
    #             print(f"  - Фильм: {film.title}")
    #     else:
    #         print("  - Нет фильмов.")