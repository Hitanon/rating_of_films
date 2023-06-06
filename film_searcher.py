import requests


class FilmSearcher:
    def __init__(self, count):
        self.file_page = 'resources/page.txt'
        self._get_number_of_page()
        self.count = count
        self.headers = {'X-API-KEY': open("resources/api_key_kinopoisk.txt", "r").read().strip('\n')}

    def get_films(self):
        url = f'https://api.kinopoisk.dev/v1.3/' \
              f'movie?selectFields=id&' \
              f'selectFields=alternativeName&' \
              f'selectFields=enName&' \
              f'selectFields=rating.kp&' \
              f'selectFields=year&' \
              f'page={self.page}&limit={self.count}'
        response = requests.get(url, headers=self.headers).json()['docs']

        films = []
        for film in response:
            film['name'] = film.get('alternativeName') or film.get('enName')
            if film['name'] is None or film['year'] is None:
                continue
            films.append(film)

        return films

    def _get_number_of_page(self):
        with open(self.file_page, 'r') as file:
            self.page = int(file.read())

    def update_number_of_page(self):
        self.page += 1
        with open(self.file_page, 'w') as file:
            file.write(str(self.page))
