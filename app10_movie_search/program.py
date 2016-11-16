from app10_movie_search.movie_client import MovieClient


def main():
    print_header()
    search_event_loop()


def print_header():
    print('----------------------------------')
    print('-------- Movie Search App --------')
    print('----------------------------------')
    print()


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        search = input('Title search text (x to exit): ')
        if search != 'x':
            client = MovieClient(search)

    print('Exiting...')


if __name__ == '__main__':
    main()