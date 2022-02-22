import json
from math import ceil

def separate_data(*same_list, **same_dict):
    len_list = ceil(len(same_list) / len(same_dict))
    new_dict = dict()
    start = 0
    finish = len_list
    for _, value in same_dict.items():
        new_dict[value] = list(same_list[start : finish])
        start += len_list
        finish += len_list
    return new_dict

def load_dict(data, json_path):
    with open(json_path, 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    n_dict = separate_data(1, 2, 3, 4, 5, name='name', make='make', made='made')
    load_dict(n_dict, 'HW_Result_2.json')

