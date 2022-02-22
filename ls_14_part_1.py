import json

def open_json_load(file_name: str):
    with open(file_name, 'r') as json_file:
        return json.load(json_file)

def write_json_dump(file_name: str, data: dict):
        with open(file_name, 'w') as file:
            json.dump(data, file)


def read_json_file(file_name: str):
    employee_data = open_json_load(file_name)

    new_employee_list = []

    for employee in employee_data['employee']:
        employee.update({'full_name': employee['firstName'] + ' ' + employee['lastName']})
        new_employee_list.append(tuple({key: value} for key, value in employee.items()))

    new_json_file = {'employee': new_employee_list}
    return(new_json_file)

write_json_dump('HW_Result_p1.json', read_json_file('HW.json'))