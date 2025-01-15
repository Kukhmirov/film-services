import datetime
from src import db, app
from src.database.models import Film, Actor

# Моковые данные для заполнения базы данных
mock_data = [
    {
        'title': 'The Shawshank Redemption',
        'release_date': datetime.date(1994, 9, 23),
        'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
        'distributed_by': 'Columbia Pictures',
        'film_length': 142.0,
        'rating': 9.3
    },
    {
        'title': 'The Godfather',
        'release_date': datetime.date(1972, 3, 24),
        'description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
        'distributed_by': 'Paramount Pictures',
        'film_length': 175.0,
        'rating': 9.2
    },
    {
        'title': 'The Dark Knight',
        'release_date': datetime.date(2008, 7, 18),
        'description': 'When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.',
        'distributed_by': 'Warner Bros. Pictures',
        'film_length': 152.0,
        'rating': 9.0
    },
    {
        'title': 'Pulp Fiction',
        'release_date': datetime.date(1994, 10, 14),
        'description': 'The lives of two mob hitmen, a boxer, a gangster\'s wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
        'distributed_by': 'Miramax Films',
        'film_length': 154.0,
        'rating': 8.9
    },
    {
        'title': 'Forrest Gump',
        'release_date': datetime.date(1994, 7, 6),
        'description': 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal, and other historical events unfold from the perspective of an Alabama man with an IQ of 75.',
        'distributed_by': 'Paramount Pictures',
        'film_length': 142.0,
        'rating': 8.8
    },
    {
        'title': 'Inception',
        'release_date': datetime.date(2010, 7, 16),
        'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.',
        'distributed_by': 'Warner Bros. Pictures',
        'film_length': 148.0,
        'rating': 8.8
    },
    {
        'title': 'The Matrix',
        'release_date': datetime.date(1999, 3, 31),
        'description': 'When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth—the life he knows is the elaborate deception of an evil cyber-intelligence.',
        'distributed_by': 'Warner Bros. Pictures',
        'film_length': 136.0,
        'rating': 8.7
    },
    {
        'title': 'Fight Club',
        'release_date': datetime.date(1999, 10, 15),
        'description': 'An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into something much, much more.',
        'distributed_by': '20th Century Fox',
        'film_length': 139.0,
        'rating': 8.8
    },
    {
        'title': 'The Lord of the Rings: The Fellowship of the Ring',
        'release_date': datetime.date(2001, 12, 19),
        'description': 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.',
        'distributed_by': 'New Line Cinema',
        'film_length': 178.0,
        'rating': 8.8
    },
    {
        'title': 'The Lord of the Rings: The Two Towers',
        'release_date': datetime.date(2002, 12, 18),
        'description': 'Gandalf, Aragorn, Legolas, and Gimli fight Saruman\'s armies, while Frodo and Sam continue their journey to Mount Doom. Swords and magic lead the battle for the fate of Middle-earth.',
        'distributed_by': 'New Line Cinema',
        'film_length': 179.0,
        'rating': 8.7
    },
    {
        'title': 'The Social Network',
        'release_date': datetime.date(2010, 10, 1),
        'description': 'The story of how Harvard student Mark Zuckerberg created Facebook, the social networking site that would become a global phenomenon.',
        'distributed_by': 'Columbia Pictures',
        'film_length': 120.0,
        'rating': 7.7
    }
]

mock_actors = [
    {'name': 'Robert Downey Jr.', 'birth_date': datetime.date(1965, 4, 4), 'is_active': True},
    {'name': 'Scarlett Johansson', 'birth_date': datetime.date(1984, 11, 22), 'is_active': True},
    {'name': 'Leonardo DiCaprio', 'birth_date': datetime.date(1974, 11, 11), 'is_active': True},
    {'name': 'Meryl Streep', 'birth_date': datetime.date(1949, 6, 22), 'is_active': False},
    {'name': 'Tom Hanks', 'birth_date': datetime.date(1956, 7, 9), 'is_active': True},
    {'name': 'Morgan Freeman', 'birth_date': datetime.date(1937, 6, 1), 'is_active': True},
    {'name': 'Tim Robbins', 'birth_date': datetime.date(1958, 10, 16), 'is_active': True},
    {'name': 'Marlon Brando', 'birth_date': datetime.date(1924, 4, 3), 'is_active': False},
    {'name': 'Al Pacino', 'birth_date': datetime.date(1940, 4, 25), 'is_active': True},
    {'name': 'Christian Bale', 'birth_date': datetime.date(1974, 1, 30), 'is_active': True},
    {'name': 'Heath Ledger', 'birth_date': datetime.date(1979, 4, 4), 'is_active': False},
    {'name': 'John Travolta', 'birth_date': datetime.date(1954, 2, 18), 'is_active': True},
    {'name': 'Uma Thurman', 'birth_date': datetime.date(1970, 4, 29), 'is_active': True},
    {'name': 'Keanu Reeves', 'birth_date': datetime.date(1964, 9, 2), 'is_active': True},
    {'name': 'Brad Pitt', 'birth_date': datetime.date(1963, 12, 18), 'is_active': True},
    {'name': 'Edward Norton', 'birth_date': datetime.date(1969, 8, 18), 'is_active': True},
    {'name': 'Elijah Wood', 'birth_date': datetime.date(1981, 1, 28), 'is_active': True},
    {'name': 'Ian McKellen', 'birth_date': datetime.date(1939, 5, 25), 'is_active': True},
    {'name': 'Jesse Eisenberg', 'birth_date': datetime.date(1983, 10, 5), 'is_active': True},
    {'name': 'Andrew Garfield', 'birth_date': datetime.date(1983, 8, 20), 'is_active': True}
]

film_actor_mapping = {
    'The Shawshank Redemption': ['Morgan Freeman', 'Tim Robbins'],
    'The Godfather': ['Marlon Brando', 'Al Pacino'],
    'The Dark Knight': ['Christian Bale', 'Heath Ledger'],
    'Pulp Fiction': ['John Travolta', 'Uma Thurman'],
    'Forrest Gump': ['Tom Hanks'],
    'Inception': ['Leonardo DiCaprio'],
    'The Matrix': ['Keanu Reeves'],
    'Fight Club': ['Brad Pitt', 'Edward Norton'],
    'The Lord of the Rings: The Fellowship of the Ring': ['Elijah Wood', 'Ian McKellen'],
    'The Social Network': ['Jesse Eisenberg', 'Andrew Garfield']
}

def seed_database():
    """Создание базы данных и добавление тестовых данных."""
    with app.app_context():
        print("Добавляем моковые данные...")

        actor_objects = {}
        # Добавляем актёров, если они ещё не добавлены
        for actor_data in mock_actors:
            actor = Actor.query.filter_by(name=actor_data['name']).first()
            if not actor:  # если актёр не существует в базе
                actor = Actor(
                    name=actor_data['name'],
                    birth_date=actor_data['birth_date'],
                    is_active=actor_data['is_active']
                )
                db.session.add(actor)
                print(f"Добавлен актёр: {actor_data['name']}")
            actor_objects[actor_data['name']] = actor
        try:
            db.session.commit()
            print("Актёры успешно добавлены.")
        except Exception as e:
            print(f"Ошибка при добавлении актёров: {e}")
            db.session.rollback()

        # Добавляем фильмы, если они ещё не добавлены
        for film_data in mock_data:
            film = Film.query.filter_by(title=film_data['title']).first()
            if not film:  # если фильм не существует в базе
                film = Film(
                    title=film_data['title'],
                    release_date=film_data['release_date'],
                    description=film_data['description'],
                    distributed_by=film_data['distributed_by'],
                    film_length=film_data['film_length'],
                    rating=film_data['rating'],
                    actors=[]
                )
                print(f"Добавлен фильм: {film_data['title']}")

                # Связываем актёров с фильмом
                actor_names = film_actor_mapping.get(film_data['title'], [])
                for name in actor_names:
                    actor = actor_objects.get(name)
                    if actor and actor not in film.actors:  # Проверяем, что актёр не добавлен
                        film.actors.append(actor)

                db.session.add(film)  # Добавляем фильм в сессию
        try:
            db.session.commit()  # Фиксируем изменения
            print("База данных успешно заполнена!")
        except Exception as e:
            print(f"Произошла ошибка при добавлении данных: {e}")
            db.session.rollback()

if __name__ == '__main__':
    seed_database()
