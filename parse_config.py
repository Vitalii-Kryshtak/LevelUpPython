def read_file_to_config_dict(path: str) -> dict:
    config = {}
    with open(path, 'r') as file:
        for line in file:
            key, val = line.strip().split(" = ")
            config[key] = val
        return config

def update_config_dict(new_config: dict, config: dict) -> dict:
    for key, val in new_config.items():
        if config.get(key) != None:
            config[key] = val
    return config

def write_config_dict_to_file(config: dict, path: str) -> None:
    with open(path, 'w') as file:
        for key, val in config.items():
            file.write(f"{key} = {val}\n")

if __name__ == "__main__":
    path = 'my_config.cfg'
    new_config = {
        'font': 'Arial',
        'font_size': 32,
        'learning': 'Science',
        'day_off': 'Monday',
        'phone': 6765723657
    }
    config = read_file_to_config_dict(path)
    config = update_config_dict(new_config, config)
    write_config_dict_to_file(config, path)

"""
Или можно тоже самое только используя декоратор

def read_file_to_config_dict(func) -> dict:
    def wrapper (new_config, path):
        config = {}
        with open(path, 'r') as file:
            for line in file:
                key, val = line.strip().split(" = ")
                config[key] = val
        return func(new_config, config, path)
    return wrapper

def update_config_dict(func) -> dict:
    def wrapper(new_config: dict, config: dict, path):
        for key, val in new_config.items():
            if config.get(key) != None:
                config[key] = val
        return func(config, path)
    return wrapper

@read_file_to_config_dict
@update_config_dict
def write_config_dict_to_file(config_dict: dict, path: str) -> None:
    with open(path, 'w') as file:
        for key, val in config_dict.items():
            file.write(f"{key} = {val}\n")

if __name__ == "__main__":
    path = 'my_config.cfg'
    new_config = {
        'font': 'Arial',
        'font_size': 32,
        'learning': 'Science',
        'day_off': 'Monday',
        'phone': 6765723657
    }```
    write_config_dict_to_file(new_config, path)
    
"""