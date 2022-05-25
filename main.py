import os
import telegram
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv("TOKEN")
    chat_id = "@cosmos_py"
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
    photo = open('images/nasax_1..jpg', 'rb')
    bot.send_photo(chat_id, photo)