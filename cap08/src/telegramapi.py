#!/usr/bin/env python3
import requests

URL = 'https://api.telegram.org/bot{}'

class TelegramApi():
    def __init__(self, token):
        self._token = token

    def send_message(self, chat_id, message, reply_markup=None):
        url = URL.format(self._token) + '/sendMessage'
        data = {'chat_id': chat_id, 'text': message, 'parse_mode': 'HTML'}
        if reply_markup:
            data['reply_markup'] = reply_markup
        r = requests.post(url, data=data)
        if r.status_code == 200:
            return r.json()
        return None
