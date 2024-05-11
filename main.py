def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_data(book_path)
    words = count_words(file_contents)
    print(f"{words} words were found in the book!")
    total_count = count_letters(file_contents)
    print(total_count)

def get_book_data(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_letters(book_text):
    lowercase_text = book_text.lower()
    letter_count = {}

    for char in lowercase_text:
        if not char in letter_count:
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



