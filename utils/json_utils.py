import json
import rate_parameters as rp

PATH = 'data/rating_of_films.txt'


def save_json(response):
    with open(PATH, 'a') as file:
        for details in response.values():
            json.dump(details, file)
            file.write('\n')


def add_ids(response, films):
    for movie in response:
        try:
            title = remove_date(movie)
            id = find_film_by_name(title, films)['id']
            response[movie] = {'id': id, **response[movie]}
        except Exception:
            continue


def replace_params_with_ids(response):
    for title, details in response.items():
        for param, values in details.items():
            replace_param_values(details, param)


def replace_param_values(details, param):
    if isinstance(details[param], list):
        for i in range(len(details[param])):
            try:
                details[param][i] = getattr(rp, param)[details[param][i]]
            except Exception:
                continue
    else:
        try:
            details[param] = globals()[param][details[param]]
        except Exception:
            pass


def remove_date(string):
    if '(' in string and ')' in string:
        start = string.rfind('(')
        end = string.rfind(')')
        return string[:start].strip()
    else:
        return string


def find_film_by_name(name, films):
    for film in films:
        if film['name'] == name:
            return film
    return None


