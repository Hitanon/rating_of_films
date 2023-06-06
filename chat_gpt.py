import json
import openai


openai.api_key = open("resources/api_key_chat_gpt.txt", "r").read().strip('\n')


class ChatGPT:
    def __init__(self, prompt_file):
        self.prompt = None
        self.prompt_file = prompt_file
        self.insert_place = '<FILMS>'
        self._read_prompt_from_file()

    def send_request(self):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": self.prompt}],
            temperature=0.1
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

    def save_response(self):
        pass

