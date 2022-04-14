import json
import yaml


def symbol_replacer(arg):
    symbols = {
        ',': '\n',
        '"': '',
        '{': '{\n',
        '}': '\n}',
        'False': 'false',
        'True': 'true'
    }
    for key in symbols:
        arg = arg.replace(key, symbols[key])
    return arg


def format_parcer(arg):
    if arg.lower().endswith(('.json')):
        data = json.load(open(arg))
    if arg.lower().endswith(('.yml', '.yaml')):
        data = yaml.load(open(arg), Loader=yaml.Loader)
    return data


def generate_diff(first_file, second_file):
    data1 = format_parcer(first_file)
    data2 = format_parcer(second_file)
    result = {}
    for key, value in data1.items():
        if key not in data2:
            result[f'  - {key}'] = str(value)
    for k2, v2 in data2.items():
        if k2 not in data1:
            result[f'  + {k2}'] = str(v2)
        elif data2[k2] != data1[k2]:
            result[f'  - {k2}'] = str(data1[k2])
            result[f'  + {k2}'] = str(v2)
        else:
            result[f'    {k2}'] = str(v2)
    sorted_result = {k: v for k, v in sorted(result.items(),
                     key=lambda item: str(item[0])[4])}
    final = json.dumps(sorted_result, separators=(',', ': '))
    final = symbol_replacer(final)
    return final
