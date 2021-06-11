from collections import defaultdict
from os.path import relpath
import django
import os
from shutil import copy2, rmtree

from task_2 import myyaml, parse, startapps

root_dir = 'my_project'
both_tpls = os.path.join(root_dir, 'templates')

if not os.path.exists(root_dir):
    structure = parse(myyaml('config_task_3.yaml'))
    startapps(structure)

django_tpls = []

for root, dirs, files in os.walk(root_dir):
    for file in files:
        rel_path = os.path.join(root, file)
        if rel_path.split('/')[1] == 'templates':
            continue
        if rel_path.find('templates') != -1:
            django_tpls.append(rel_path)

if os.path.exists(both_tpls):
    rmtree(both_tpls)

for tpl in django_tpls:
    new_path_tpl = os.path.join(root_dir, os.path.join(*tpl.split('/')[2::]))
    new_dirs = os.path.split(new_path_tpl)
    if not os.path.exists(new_dirs[0]):
        os.makedirs(new_dirs[0])
    copy2(tpl, new_path_tpl)
    print(tpl + '--->' + new_path_tpl + '--->' + new_dirs[0])
