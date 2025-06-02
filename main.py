from stats import get_num_words
from stats import get_char_count
from stats import get_sorted_list
import sys

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    return file_contents


def main():
    # if sys.arv doesn't have two entries
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        raise SystemExit[1]
    #use second argument as file path
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = get_num_words(book_text)
    char_count = get_char_count(book_text)
    char_list = get_sorted_list(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_list:
        temp_dict = item
        character = item["char"]
        number = item["num"]
        print(f"{character}: {number}")
    
    #print(char_list)
    print("============= END ===============")




main()