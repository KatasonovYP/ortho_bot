import json
import os


def download(path=os.environ.get('PATH_TO_DATA')):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    return data