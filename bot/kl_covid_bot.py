import requests
import dotenv
import os
import json

dotenv.load_dotenv()


class TelegramBot:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_TOKEN")
        self.base_url = f"https://api.telegram.org/bot{self.token}/"

    def get_updates(self, offset=None):
        url = self.base_url + "getUpdates?timeout=60"
        if offset:
            url = url + f"&offset={offset+1}"
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = (
            self.base_url
            + f"sendMessage?chat_id={chat_id}&text={msg}&parse_mode={'HTML'}"
        )
        if msg:
            requests.get(url)
