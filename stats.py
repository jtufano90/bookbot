def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    count = 0
    split_text = get_book_text(book_text).split()
    for i in split_text:
        count += 1
    print(f"Found {count} total words")

def count_char(text):
    char_dict = {}
    new_text = text.lower()
    for i in new_text:
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1
    return char_dict

def sort_dict(dict):
    return dict["count"]

def chars_dict_sorted_list(char_counts):
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse = True, key = sort_dict)
    return chars_list