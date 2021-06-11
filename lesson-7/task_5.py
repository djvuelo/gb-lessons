import os
from collections import OrderedDict
import json

import django

root_dir = django.__path__[0]
django_files = {}
for root, dirs, files in os.walk(root_dir):
    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        rel_path = os.path.join(root, file)
        size = os.stat(rel_path).st_size
        size = 10 ** len(str(size))
        django_files.setdefault(size, []).append(ext)

django_files = {file: (len(django_files[file]), list(set(django_files[file]))) for file in django_files}
django_files = dict(OrderedDict(sorted(django_files.items(), key=lambda t: t[0])))

print(django_files, sep='\n')

with open('dir_stats.json', 'w', encoding='UTF-8') as json_file:
    json.dump(django_files, json_file)
