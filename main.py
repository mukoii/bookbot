"""
Filename: <main.py>
Author: <Nathan Delcampo>
Created: <2025-12-24>
Description:
 Main python executable for boot.dev BookBot python project
"""

from stats import *
import sys 

def main():
    if not (len(sys.argv) >= 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    filepath = sys.argv[1]

    # Get data from given filepath
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    sorted_characters = sort_dict(num_characters)

    print(f"============ BOOKBOT ============" )
    print(f"Analyzing book found at {filepath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for dictionary in sorted_characters:
        if not dictionary["char"].isalpha():
            continue
        print(f"{dictionary["char"]}: {dictionary["num"]}")


main()