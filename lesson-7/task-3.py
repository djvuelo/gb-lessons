from socket import socket

from task_2 import myyaml, parse, startapps

# import os
# from collections import defaultdict
# from os.path import relpath
#
# import django
#
# root_dir = 'my_project'
# django_files = defaultdict(list)
#
# for root, dirs, files in os.walk(root_dir):
#    for file in files:
#        ext = file.rsplit('.', maxsplit=1)[-1].lower()
#        rel_path = relpath(os.path.join(root, file), root_dir)
#        django_files[ext].append(rel_path)
#
# for ext, files in sorted(django_files.items(),
#                         key=lambda x: len(x[1]), reverse=True):
#
#    print(f'{ext}: {len(files)}')
#
# print('\nPY FILES')
# print(*sorted(django_files['html'])[:10], sep='\n')


structure = parse(myyaml('config_task_3.yaml'))
startapps(structure)

root_project = 'my_project'

