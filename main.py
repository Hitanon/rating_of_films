import argparse
import time

from chat_gpt import ChatGPT
from film_searcher import FilmSearcher
import utils.json_utils as utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--cnt_pages', type=int, default=10,
                        help='Number of pages to process')
    args = parser.parse_args()

    CNT_PAGES = args.cnt_pages

    film_searcher = FilmSearcher(20)
    chat_gpt = ChatGPT("resources/prompt.txt")

    cnt_pages = film_searcher.page + CNT_PAGES
    while film_searcher.page < cnt_pages:
        try:
            films = film_searcher.get_films()
        except Exception:
            time.sleep(60)
            continue
        print(films)
        chat_gpt.fill_prompt(films)
        try:
            response = chat_gpt.send_request()
        except Exception:
            print('Error with open-ai API')
            break
        utils.add_ids(response, films)
        utils.replace_params_with_ids(response)
        utils.save_json(response)
        film_searcher.update_number_of_page()
        print(response)
