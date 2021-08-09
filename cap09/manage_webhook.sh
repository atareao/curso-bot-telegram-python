#!/bin/bash
option=$1

while IFS='=' read -r variable value
do
    export "${variable}"="${value}"
done < curso.env

case "${option}" in
    get)
        curl "https://api.telegram.org/bot${TELEGRAM_API_TOKEN}/getWebhookInfo"
        ;;
    set)
        echo "${BASE_URI}/webhook/${WEBHOOK}"
        curl -F "url=${BASE_URI}/webhook/${WEBHOOK}" "https://api.telegram.org/bot${TELEGRAM_API_TOKEN}/setWebhook"
        ;;
    delete)
        curl "https://api.telegram.org/bot${TELEGRAM_API_TOKEN}/deleteWebhook"
        ;;
    *)
        echo "Set an option: 'set', 'get', 'delete'"
        ;;
esac

