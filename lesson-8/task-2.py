import requests
from os import path
import re

RE_LOGS = re.compile(r'((?:[a-z0-9:\.]+))[\s-]+\[((?:.+))\]\s"((?:[a-z]+))\s((?:\S+))\s.+"\s((?:\d+))\s((?:\d+))\s',
                     re.IGNORECASE)

if not path.exists('server_logs.txt'):
    print('Скачивание файла логов ...')
    server_logs_responce = requests.get(
        'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text
    with open('server_logs.txt', 'w', encoding='UTF-8') as server_logs:
        server_logs.write(server_logs_responce)
    print('Логи успешно скачаны.')

with open('server_logs.txt', 'r', encoding='UTF-8') as server_logs:
    for server_log in server_logs:
        print(*RE_LOGS.findall(server_log))
