import json


def get_users(file: str = "data/users.json") -> list:
    try:
        with open(file, 'r') as f:
            users = json.load(f)
    except:
        users = []
    return users


def write_data(data: list, file: str = "data/users.json") -> str:
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
    return "Ma'lumot qo'shildi!"
