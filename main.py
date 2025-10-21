import sys

from stats import (
    get_num_words,
    get_num_chars,
    sort_dict
)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    content = get_book_text(path)
    words = get_num_words(content)
    characters = get_num_chars(content)
    sorted_dictionary = sort_dict(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(words)
    print("--------- Character Count -------")
    for item in sorted_dictionary:
        ch = item["char"]
        val = item["num"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {val}")
    print("============= END ===============")

main()