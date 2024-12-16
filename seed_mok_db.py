import datetime
import uuid
from src import db, app  # Импорты вашего приложения и базы данных
from src.models import Film  # Импорт модели Film

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
        'title': 'The Social Network',
        'release_date': datetime.date(2010, 10, 1),
        'description': 'The story of how Harvard student Mark Zuckerberg created Facebook, the social networking site that would become a global phenomenon.',
        'distributed_by': 'Columbia Pictures',
        'film_length': 120.0,
        'rating': 7.7
    }
]

def seed_database():
    """Создание базы данных и добавление тестовых данных."""
    with app.app_context():
        print("Добавляем моковые данные...")
        for film_data in mock_data:
            film = Film(
                title=film_data['title'],
                release_date=film_data['release_date'],
                description=film_data['description'],
                distributed_by=film_data['distributed_by'],
                film_length=film_data['film_length']
            )
            film.rating = film_data['rating']
            db.session.add(film)  # Добавляем каждый фильм в сессию

        try:
            db.session.commit()  # Фиксируем изменения
            print("База данных успешно заполнена!")
        except Exception as e:
            print(f"Произошла ошибка при добавлении данных: {e}")
            db.session.rollback()

if __name__ == '__main__':
    seed_database()
