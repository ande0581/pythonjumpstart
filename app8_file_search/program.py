import os
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry we can't search that location")
        return

    text = get_search_text_from_user()
    if not text:
        print("No text enter, we can't search for nothing")

    matches = search_folders(folder, text)
    for m in matches:
        print('-----------------------MATCH------------------------')
        print('file: {}'.format(m.file))
        print('line: {}'.format(m.line))
        print('match: {}'.format(m.text.strip()))
        print()


def print_header():
    print('--------------------------------------')
    print('           File Search App')
    print('--------------------------------------')


def get_folder_from_user():
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]? ')
    return text.lower()


def search_folders(folder, text):

    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):  # We use recursion to search through folder hierarchy
            yield from search_folders(full_item, text)  # This is generator method new to python 3.3
        else:  # this searches individual files
            yield from search_file(full_item, text)


def search_file(filename, search_text):
    with open(filename, 'r', encoding='utf-8') as fin:  # utf-8 makes sure we are only searching text

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                yield m


if __name__ == '__main__':
    main()