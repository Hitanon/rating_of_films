import json
import openai


def load_api_key(line_number):
    with open("resources/api_key_chat_gpt.txt", "r") as file:
        for i, line in enumerate(file):
            if i == line_number - 1:
                openai.api_key = line.strip('\n')
                break


class ChatGPT:
    def __init__(self, prompt_file, number_of_key):
        self.prompt = None
        self.prompt_file = prompt_file
        self.insert_place = '<FILMS>'
        self._read_prompt_from_file()
        load_api_key(number_of_key)

    def send_request(self):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": self.prompt}],
            temperature=0.08
        )
        response_text = response['choices'][0]['message']['content']
        print(response_text)
        return json.loads(response_text)

    def fill_prompt(self, films):
        self._read_prompt_from_file()
        film_titles = [f'{film["name"]} ({film["year"]})' for film in films]
        self.prompt = self.prompt.replace(self.insert_place, ';\n'.join(film_titles))

    def _read_prompt_from_file(self):
        with open(self.prompt_file, 'r') as f:
            self.prompt = f.read()

