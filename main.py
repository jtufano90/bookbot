import sys
from stats import count_words, count_char, sort_dict, chars_dict_sorted_list

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_text(sys.argv[1]))

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    char_counts = count_char(text)
    sorted_chars = chars_dict_sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")

    count_words(sys.argv[1])

    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")