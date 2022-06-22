import os
import telegram
from dotenv import load_dotenv
from time import sleep


def send_message(directory, chat_id , publication_delay_time):
    for root, dirs, files in os.walk(directory):
        for filee in files:
            file = filee
            photo = open(f"{directory}/{file}", 'rb')
            bot.send_photo(chat_id, photo)
            sleep(publication_delay_time)


def un_flood(directory, chat_id , publication_delay_time):
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
    un_flood(directory, chat_id , publication_delay_time)
