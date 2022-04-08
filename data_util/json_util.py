import json

def read_json(source_file_path):
    with open(source_file_path, 'r') as source_file:
        return json.load(source_file)

def write_json(data, target_file_path):
    with open(target_file_path, 'w') as target_file:
        json.dump(data, target_file, indent=4)

if __name__ == '__main__':
    data = read_json('./data-tasks/data/beatles.json')
    data = {key: {'first_name': name['first_name'], 'last_name': name['last_name'].upper()} for key, name in data.items()}
    write_json(data, './data-tasks/data/beatles_upper.json')