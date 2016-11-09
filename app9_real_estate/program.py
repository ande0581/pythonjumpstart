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


# def get_price(p):
#     return p.price


def query_data(data):

    # if data was sorted by price:
    for p in data:
        print(p.price)
    data.sort(key=lambda p: p.price)

    # most expensive house
    high_purchase = data[-1]
    print('The most expensive house is ${:,} with {} beds and {} baths'.format(high_purchase.price, high_purchase.beds,
                                                                               high_purchase.baths))

    # lease expensive house
    low_purchase = data[0]
    print('The least expensive house is ${:,} with {} beds and {} baths'.format(low_purchase.price, low_purchase.beds,
                                                                                low_purchase.baths))

    # average house price
    # average price of 2 bedroom houses


if __name__ == '__main__':
    main()