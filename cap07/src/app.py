#!/usr/bin/env python3
from flask import Flask, jsonify, make_response, request
from telegramapi import TelegramApi
import time
import os
import sys
import re
import json


app = Flask(__name__)

telegramApi = TelegramApi(os.environ['TELEGRAM_API_TOKEN'])

def logger(message):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    sys.stdout.write('{} | {}\n'.format(timestamp, message))


@app.route('/status', methods=['GET'])
def get_status():
    return 'Up and running', 201

@app.route('/webhook/<webhook>', methods=['GET', 'POST'])
def get_webhook(webhook):
    logger(webhook)
    if os.environ['WEBHOOK'] != webhook:
        return 'KO', 404
    try:
        if request.method == 'GET' or not request.json:
            return 'OK', 200
    except Exception:
        return 'OK', 200
    payload = request.json
    logger(json.dumps(payload, indent=4, sort_keys=True))
    return 'OK', 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
