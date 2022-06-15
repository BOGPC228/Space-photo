import os
import telegram
from dotenv import load_dotenv
from time import sleep


def send_message(directory, chat_id ,time_day):
    for root, dirs, files in os.walk(directory):
        for filee in files:
            file = filee
            photo = open(f"{directory}/{file}", 'rb')
            bot.send_photo(chat_id, photo)
            sleep(time_day)


def un_flood(directory, chat_id ,time_day):
    while True:
        send_message(directory, chat_id ,time_day)


if __name__ == '__main__':
    load_dotenv()
    directory = "images"
    token = os.getenv("TOKEN_BOT")
    chat_id = os.getenv("CHAT_ID_TG")
    time_day = os.getenv("TIME")
    time_day = int(time_day)
    bot = telegram.Bot(token=token)
    un_flood(directory, chat_id ,time_day)
