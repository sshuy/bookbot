def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_data(book_path)
    words = count_words(file_contents)

    print(f"--- Begin report for {book_path} ---")
    print(f"{words} words were found in the book!")

    letters_in_novel = count_letters(file_contents)
    list_data = convert_dict_to_list(letters_in_novel)
    list_data.sort(reverse=True, key=sort_it)
    for data in list_data:
        print(f"The '{data['letter']}' character was found {data['num']} times")
    print("--- End Report ---")


def get_book_data(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

def convert_dict_to_list(dict):
    list = []
    for char in dict:
        num = dict[char]
        next = {"letter": char, "num": num}
        list.append(next)
    return list

def sort_it(dict):
    return dict['num']

def count_letters(book_text):
    lowercase_text = book_text.lower()
    letter_count = {}

    for char in lowercase_text:
        if char.isalpha() and not char in letter_count:
            letter_count[char] = 0
        if char in letter_count:
            count = letter_count[char]
            count += 1
            letter_count[char] = count
    return letter_count

# A better solution to the one above.
def count_letters_v2(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()



