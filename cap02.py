#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2021 Lorenzo Carbonell <a.k.a. atareao>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import requests

PROPERTIES = '.telegramkeys'

class TelegramBot():
    def __init__(self):
        self._token = None
        self._group = None
        self._channel = None
        with open(PROPERTIES, 'r') as file_reader:
            params = json.load(file_reader)
            self._token = params['token']
            self._group = params['group']
            self._channel = params['channel']

    def get_me(self):
        url = f"https://api.telegram.org/bot{self._token}/getMe"
        response = requests.get(url)
        if response.status_code == 200:
            salida = json.loads(response.text)
            return salida
        return None

    def get_updates(self):
        url = f"https://api.telegram.org/bot{self._token}/getUpdates"
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            salida = json.loads(response.text)
            return salida
        return None

    def send_message_to_group(self, message, parse_mode='HTML'):
        try:
            return self.send_message(self._group, message, parse_mode)
        except Exception as exception:
            print(exception)
        return None

    def send_message_to_channel(self, message, parse_mode='HTML'):
        try:
            return self.send_message(self._channel, message, parse_mode)
        except Exception as exception:
            print(exception)
        return None

    def send_message(self, chat_id, message, parse_mode='HTML'):
        url = f"https://api.telegram.org/bot{self._token}/sendMessage"
        data = {"chat_id": chat_id, "text": message, "parse_mode": parse_mode,
                "disable_web_page_preview": True}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            salida = json.loads(response.text)
            return salida
        error = json.loads(response.text)
        error_code = error['error_code']
        description = error['description']
        msg = f"Error: {error_code}. Description: {description}"
        raise Exception(msg)

    def set_chat_title(self, chat_id, title):
        url = f"https://api.telegram.org/bot{self._token}/setChatTitle"
        data = {"chat_id": chat_id, "title": title}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            salida = json.loads(response.text)
            return salida
        error = json.loads(response.text)
        error_code = error['error_code']
        description = error['description']
        msg = f"Error: {error_code}. Description: {description}"
        raise Exception(msg)

    def set_group_title(self, title):
        try:
            return self.set_chat_title(self._group, title)
        except Exception as exception:
            print(exception)
        return None

    def set_channel_title(self, title):
        try:
            return self.set_chat_title(self._channel, title)
        except Exception as exception:
            print(exception)
        return None

    def set_chat_description(self, chat_id, description):
        url = f"https://api.telegram.org/bot{self._token}/setChatDescription"
        data = {"chat_id": chat_id, "description": description}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            salida = json.loads(response.text)
            return salida
        error = json.loads(response.text)
        error_code = error['error_code']
        description = error['description']
        msg = f"Error: {error_code}. Description: {description}"
        raise Exception(msg)

    def set_group_description(self, description):
        try:
            return self.set_chat_description(self._group, description)
        except Exception as exception:
            print(exception)
        return None


    def set_channel_description(self, description):
        try:
            return self.set_chat_description(self._channel, description)
        except Exception as exception:
            print(exception)
        return None

    def pin_message(self, chat_id, message_id, disable_notification=False):
        url = f"https://api.telegram.org/bot{self._token}/pinChatMessage"
        data = {"chat_id": chat_id, "message_id": message_id,
                "disable_notification": disable_notification}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            salida = json.loads(response.text)
            return salida
        error = json.loads(response.text)
        error_code = error['error_code']
        description = error['description']
        msg = f"Error: {error_code}. Description: {description}"
        raise Exception(msg)

    def pin_message_in_group(self, message_id, disable_notification=False):
        try:
            return self.pin_message(self._group, message_id,
                                    disable_notification)
        except Exception as exception:
            print(exception)
        return None


    def pin_message_in_channel(self, message_id, disable_notification=False):
        try:
            return self.pin_message(self._channel, message_id,
                                    disable_notification)
        except Exception as exception:
            print(exception)
        return None

    def unpin_message(self, chat_id, message_id):
        url = f"https://api.telegram.org/bot{self._token}/unpinChatMessage"
        data = {"chat_id": chat_id, "message_id": message_id}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            salida = json.loads(response.text)
            return salida
        error = json.loads(response.text)
        error_code = error['error_code']
        description = error['description']
        msg = f"Error: {error_code}. Description: {description}"
        raise Exception(msg)

    def unpin_message_in_group(self, message_id):
        try:
            return self.unpin_message(self._group, message_id)
        except Exception as exception:
            print(exception)
        return None


    def unpin_message_in_channel(self, message_id):
        try:
            return self.unpin_message(self._channel, message_id)
        except Exception as exception:
            print(exception)
        return None



if __name__ == "__main__":
    tb = TelegramBot()
    # print(tb.get_me())
    # print(tb.get_updates())
    # print(tb.send_message_to_group("Hola grupo"))
    # print(tb.send_message_to_channel("Hola canal"))
    # print(tb.send_message_to_channel("Hola <b>canal</b>"))
    # print(tb.send_message_to_channel("Hola _canal_", "MarkdownV2"))
    # print(tb.send_message_to_channel("[atareao\.es](https://atareao.es/tutorial/crea-tu-propio-bot-para-telegram/bot-en-python-para-telegram/)", "MarkdownV2"))
    # print(tb.set_channel_title("atcursobot"))
    # print(tb.set_channel_description("descripción de un canal interesante"))
    # print(tb.unpin_message_in_channel("36"))
