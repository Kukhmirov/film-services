import http
import json
from dataclasses import dataclass
from unittest.mock import patch

from src import app

@dataclass
class FakeFilm:
    title = 'Fake Film'
    distributed_by = 'test company'
    release_date = '2010-04-01'
    description = 'Fake description'
    film_length = 100
    rating = 8.0

class TestFilms:
    uuid = []

    def test_get_films_with_db(self):
        client = app.test_client()
        response = client.get('/films')

        assert response.status_code == http.HTTPStatus.OK

    @patch('src.services.film_service.FilmService.fetch_all_films', autospec=True)
    def test_get_films_mock_db(self, mock_get_films_mock):
        click = app.test_client()
        response = click.get('/films')
        mock_get_films_mock.assert_called_once()
        assert response.status_code == http.HTTPStatus.OK
        assert len(response.json) == 0

    def test_create_film_with_db(self):
        client = app.test_client()
        data = {
            'title': 'test title',
            'distributed_by': 'test company',
            'release_date': '2010-04-01',
            'description': '',
            'film_length': 100,
            'rating': 8.0,
        }

        response = client.post('/films', data=json.dumps(data), content_type='application/json')

        assert response.status_code == http.HTTPStatus.CREATED
        assert response.json['title'] == 'test title'
        self.uuid.append(response.json['uuid'])

    def test_create_film_with_mock_db(self):
        with patch('src.db.session.add', autospec=True) as mock_session_add, \
                patch('src.db.session.commit', autospec=True) as mock_session_commit:
            client = app.test_client()
            data = {
                'title': 'test title',
                'distributed_by': 'test company',
                'release_date': '2010-04-01',
                'description': '',
                'film_length': 100,
                'rating': 8.0,
            }
            response = client.post('/films', data=json.dumps(data), content_type='application/json')
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()
    def test_update_film_with_db(self):
        client = app.test_client()
        url = f'/films/{self.uuid[0]}'
        data = {
            'title': 'test updated title',
            'distributed_by': 'test updated company',
            'release_date': '2010-04-01',
        }
        response = client.put(url, data=json.dumps(data), content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK
        assert response.json['title'] == 'test updated title'
    def test_update_film_with_nock_db(self):
        with patch('src.services.film_service.FilmService.fetch_film_by_uuid') as mocked_query, \
                patch('src.db.session.add', autospec=True) as mock_session_add, \
                patch('src.db.session.commit', autospec=True) as mock_session_commit:
            mocked_query.return_value = FakeFilm()
            client = app.test_client()
            url = f'/films/1'
            data = {
                'title': 'test updated title',
                'distributed_by': 'test updated company',
                'release_date': '2010-04-01',
            }
            response = client.put(url, data=json.dumps(data), content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK
        assert response.json['title'] == 'test updated title'
    def test_delete_film_with_db(self):
        client = app.test_client()
        url = f'/films/{self.uuid[0]}'
        response = client.delete(url)
        assert response.status_code == http.HTTPStatus.NO_CONTENT