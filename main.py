from stats import get_num_words, character_count, create_report
from sys import argv, exit

def get_book_text(filepath):
    contents = ''
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    path = argv[1]
    contents = get_book_text(path)
    num_words = get_num_words(contents)
    dict_characters = character_count(contents)
    create_report(num_words, dict_characters)

main()