import os
from pathlib import Path


def myyaml(config):
    with open(config, 'r', encoding='UTF-8') as config:
        return [line.replace('\n', '') for idx, line in enumerate(config.readlines())]


def get_location_stroke(stroke):
    if len(stroke.split('- ')) == 1:
        return 0
    else:
        return len(stroke.split('- ')[0])


def parse(config_strokes, container=[]):
    current_location = get_location_stroke(config_strokes[0])
    for idx, stroke in enumerate(config_strokes):
        now_location = get_location_stroke(stroke)

        if now_location < current_location:
            break
        if not stroke or current_location != now_location:
            continue

        value = stroke.replace('- ', '').replace(' ', '')
        if value[-1::] == ':':
            container.append({value.replace(':', ''): []})
            parse(config_strokes[(idx + 1)::], container[-1::][0][value.replace(':', '')])
        else:
            container.append(value)

    return container


def startapps(structures, files=[], path=''):
    if type(structures) == dict:
        for structure in structures:
            path = os.path.join(path, structure)

            if not os.path.exists(path):
                os.makedirs(path)

            startapps(structures[structure], files, path)
    elif type(structures) == list:
        for structure in structures:
            if type(structure) == str:
                file_path = os.path.join(path, structure)
                files.append(file_path)
                if not os.path.exists(file_path):
                    file = open(file_path, 'w', encoding='UTF-8')
                    file.close()
            else:
                startapps(structure, files, path)
    return files


if __name__ == '__main__':
    structure = parse(myyaml('config_task_2.yaml'))
    print(structure)
    startapps(structure)
else:
    pass
