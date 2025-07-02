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

# imports from stats.py the filepath, the <get_book_text> and <charc_and_count> funcs
from stats import path_to_file, get_book_text, charc_and_count

# creates a var called <file_contents> 
file_contents = get_book_text(path_to_file)

dictionary_of_chars_and_counts = charc_and_count(file_contents)
print(dictionary_of_chars_and_counts)