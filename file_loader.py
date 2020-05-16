from config import dataset


def get_data():
    with open(dataset, 'r') as fp:
        print(fp.read())