import os
import csv

from app9_real_estate.data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('---------------------------------')
    print('   Real Estate Data Mining App   ')
    print('---------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)  # this is the file that we are running for this program
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)  # this is pretty awesome
        purchases = []
        for row in reader:
            # we don't need to make instance [p = Purchase()] first now that it has a @staticmethod in class
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        # print(purchases[0].__dict__)
        return purchases


def query_data(data):
    pass


if __name__ == '__main__':
    main()