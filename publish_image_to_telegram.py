import os
import telegram
from dotenv import load_dotenv
from time import sleep


if __name__ == '__main__':
    load_dotenv()
    directory = "images"
    tg_token = os.getenv("TG_BOT_TOKEN")
    chat_id = os.getenv("TG_CHAT_ID")
    publication_delay_time = os.getenv("DELAY_TIME")
    publication_delay_time = int(publication_delay_time)
    bot = telegram.Bot(token=tg_token)
    while True:
        for file_name in os.listdir(directory):
            with open(f"{directory}/{file_name}", 'rb') as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
            sleep(publication_delay_time)
