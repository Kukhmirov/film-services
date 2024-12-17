import uuid
from src import db


class Film(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.Date, index=True, nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    description = db.Column(db.String(220))
    distributed_by = db.Column(db.String(120), nullable=False)
    film_length = db.Column(db.Float)
    rating = db.Column(db.Float)

    def __init__(self, title, release_date, description, distributed_by, film_length, rating):
        self.title = title
        self.release_date = release_date
        self.uuid = str(uuid.uuid4())
        self.description = description
        self.distributed_by = distributed_by
        self.film_length = film_length
        self.rating = rating

    def __repr__(self):
        return f"Film ({self.title}, {self.release_date}, {self.uuid}, {self.description}, {self.distributed_by}, {self.film_length}, {self.rating})"

    @property
    def release_date_str(self):
        """Преобразуем дату в строку при обращении к этому свойству"""
        return self.release_date.strftime('%Y-%m-%d') if self.release_date else None

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date_str,
            'uuid': self.uuid,
            'description': self.description,
            'distributed_by': self.distributed_by,
            'film_length': self.film_length,
            'rating': self.rating
        }

class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    birth_date = db.Column(db.Date)
    is_active = db.Column(db.Boolean, default=False)

    def __init__(self, name, birth_date, is_active):
        self.name = name
        self.birth_date = birth_date
        self.is_active = is_active

    def __repr__(self):
        return f"Actor ({self.name}, {self.birth_date}, {self.is_active})"