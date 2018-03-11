import z3


def read_data(data_path):
    import csv
    with open(data_path, 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
        	print(row)
        return dict(reader)


if __name__ == '__main__':
    print('DEBUG')

    # data test
    data = read_data('../data/example.csv')
    print(data)
