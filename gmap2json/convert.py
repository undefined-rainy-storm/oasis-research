import re
from json import dumps

while True:
    gets = input()
    read = open(gets, encoding='utf-8').read()
    pos = []
    for each in read.split('\n')[1:]:
        point_info = each.split(',')[0]
        result = re.findall(r'([0-9]{1,10}\.[0-9]{1,10})', point_info)
        print(result)
        if result and len(result) == 2:
            pos.append([*map(float, result)])
    filename = '.'.join('/'.join(gets.split('/')[1:]).split('.')[:-1]) + '.json'
    with open(f'out/{filename}', mode='w') as f:
        f.write(dumps(pos))
    if not gets:
        break
