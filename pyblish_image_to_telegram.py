import os
import telegram
from dotenv import load_dotenv
from time import sleep


def send_message(directory, chat_id , publication_delay_time):
    for file_name in os.listdir(directory):
        with open(f"{directory}/{file_name}", 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)
        sleep(publication_delay_time)


def send_endlessly_photos(directory, chat_id , publication_delay_time):
    while True:
        send_message(directory, chat_id , publication_delay_time)


if __name__ == '__main__':
    load_dotenv()
    directory = "images"
    token = os.getenv("TOKEN_BOT")
    chat_id = os.getenv("CHAT_ID_TG")
    publication_delay_time = os.getenv("DELAY_TIME")
    publication_delay_time = int(publication_delay_time)
    bot = telegram.Bot(token=token)
    send_endlessly_photos(directory, chat_id , publication_delay_time)
