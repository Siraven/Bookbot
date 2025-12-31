import sys
from stats import get_num_words, get_letter_count, format_list





def main():
    book = get_book_text(book_path)
    book_words = get_num_words(book)
    letter_count = get_letter_count(book)
    sorted_letters = format_list(letter_count)
    sorted_letters.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_words} total words")
    print("--------- Character Count -------")
    for i in sorted_letters:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


def sort_on(items):
    return items["num"]

def get_book_text(path):
    with open(path) as f:
        book = f.read()
        return book



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    main()