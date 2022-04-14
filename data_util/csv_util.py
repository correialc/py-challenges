import csv

def read_csv(source_file_path):
    with open(source_file_path, 'r') as source_file:
        data = csv.reader(source_file)
        data.__next__()
        return [tuple(row) for row in data]


def write_csv(data, target_file_path):
    with open(target_file_path, 'w') as target_file:
        csv.writer(target_file).writerows(data)


if __name__ == '__main__':
    data = [tuple([row[0], row[1].upper()]) for row in read_csv('./data-tasks/data/beatles.csv')]         
    write_csv(data, './data-tasks/data/beatles-upper.csv')
