import os
import csv
try:
    import statistics
except ImportError:  # an example of making something python2 compatible using try/except
    import app9_real_estate.statistics_standin_python2 as statistics

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
    with open(filename, 'r') as fin:

        reader = csv.DictReader(fin)  # this is pretty awesome
        purchases = []
        for row in reader:
            # we don't need to make instance [p = Purchase()] first now that it has a @staticmethod in class
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        # print(purchases[0].__dict__)
        return purchases


def query_data(data):

    # if data was sorted by price:
    data.sort(key=lambda p: p.price)

    # most expensive house
    high_purchase = data[-1]
    print('The most expensive house is ${:,.2f} with {} beds and {} baths'.format(high_purchase.price,
                                                                                  high_purchase.beds,
                                                                                  high_purchase.baths))

    # lease expensive house
    low_purchase = data[0]
    print('The least expensive house is ${:,.2f} with {} beds and {} baths'.format(low_purchase.price,
                                                                                   low_purchase.beds,
                                                                                   low_purchase.baths))

    # # List comprehension
    # two_bed_homes = [
    #     p  # projection or items
    #     for p in data  # the set to process
    #     if p.beds == 2
    # ]

    # this changes the list comprehension to a generator expression
    two_bed_homes = (
        p
        for p in data
        if announce(p, '2-bedrooms, found {}'.format(p.beds)) and p.beds == 2  # test / condition
    )

    # this method allows us to only grab the first 5 homes, the alternative would have been to grab all and then
    # do a list slice [:5]
    homes = []
    for h in two_bed_homes:
        if len(homes) >= 5:
            break
        homes.append(h)

    avg_price = statistics.mean(announce(p.price, 'price') for p in homes)
    avg_baths = statistics.mean((p.baths for p in homes))
    avg_sqft = statistics.mean((p.sq__ft for p in homes))

    print('Avg 2-Bedroom home is ${:,.2f}, baths={}, sq ft={:,}'
          .format(avg_price, round(avg_baths, 1), round(avg_sqft, 1)))


def announce(item, msg):
    print('Pulling item {} for {}'.format(item, msg))
    return item


if __name__ == '__main__':
    main()