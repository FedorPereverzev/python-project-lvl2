import json


def generate_diff(first_file, second_file):
    data1 = json.load(open(first_file))
    data2 = json.load(open(second_file))
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
    sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: str(item[0])[4])}
    final = json.dumps(sorted_result, separators=(',', ': '))
    final = final.replace(',', '\n').replace('"','').replace('{', '{\n').replace('}', '\n}').replace('False', 'false').replace('True', 'true')
    return print(final)