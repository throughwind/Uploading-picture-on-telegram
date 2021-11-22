import telegram as tg
import os
import time
from dotenv import load_dotenv


def send_photo_in_tg(photos, time_sleep):
    while True:
        for photo in photos:
            bot.send_photo(chat_id=tg_chat_id, photo=open(f"images/{photo}", 'rb'))
            time.sleep(time_sleep)


if __name__ == "__main__":
    load_dotenv()
    tg_token = os.getenv("TG_TOKEN")
    bot = tg.Bot(token=tg_token)
    time_sleep = int(os.getenv("TIME_SLEEP"))
    photos = os.listdir("images")
    tg_chat_id = os.getenv("CHAT_ID")
    send_photo_in_tg(photos, time_sleep)
