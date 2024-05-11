def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_data(book)
    words = count_words(file_contents)
    print(f"{words} words were found in the book!")

def get_book_data(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

main()