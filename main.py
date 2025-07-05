'''
from stats import filepath,get_book_text, count_char
#from stats import count_char

#filepath = "/home/bane/projects/github.com/DrBane00/bookbot/books/frankenstein.txt"

def main ():
    num_words = get_book_text(filepath)
    print(f"{len(num_words)} words found in the document")
    print(count_char(num_words))
    
main()
'''
import sys
# imports from stats.py the filepath, the <get_book_text> and <charc_and_count> funcs
from stats import get_book_text, charc_and_count, get_num_words

'''
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
else:
'''


def main ():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    # creates a var called <file_contents> 
    file_contents = get_book_text(path_to_file)
    get_num_words(file_contents, path_to_file)

    print("--------- Character Count -------")
    dictionary_of_chars_and_counts = charc_and_count(file_contents)
    print("============= END ===============")

#def sort_on(items):
 #   return items["num"]
#print(dictionary_of_chars_and_counts)
main ()