# rating_of_films
A program for evaluating films using chatGPT according to specified criteria

Настройка перед первым запуском:
1) указать ключ от API Кинопоиска в /resources/api_key_kinopoisk.txt
2) указать ключи от API openai в /resources/api_chat_gpt.txt (можно сразу несколько ключей по одному в строке)
3) указать начальную страницу с которой будет приходить результат /resources/page.txt
   (цифру в первую строку, сейчас я на 6500+ странице, поэтому можно указывать 15000+)
   
Запуск:
python main.py --cnt_pages <Количество страниц>

Работает до тех пор пока не будут получены все страницы, либо пока api openai не отправит 10 оветов с ошибкой
После каждого ответа с ошибкой переходит на использование нового api ключа
