'''
filepath = "/home/bane/projects/github.com/DrBane00/bookbot/books/frankenstein.txt"

num_words = 0
full_contents = ""
chars = set(full_contents.lower())
char_count = dict()

def get_book_text (filepath):
    with open(filepath) as f:
        contents = f.read()

    word_list = contents.split()
    num_words = len(word_list)
    return word_list

def count_char (book_text):

    #print (type(book_text))

    for element in set(book_text):
        count_of_char = 0
        for char in set(book_text):
            if char == element:
                count_of_char += 1
        char_count[element] = count_of_char

    #print (char_count)
    return char_count
'''

#from discord ... i'll try and explain each step

# finds the book
#path_to_file = ""

# creates and returns a string called <file_contents>
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

# this func aims to count the words in the book
def get_num_words(file_contents, path_to_file):
    # creates a list from a string
    words = file_contents.split()
    # counts the num of words
    num_words = len(words)
    # prints
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

# this func aims to count the frequency of each char in the book
def charc_and_count(file_contents):

    # creates an empty dict
    charc_count_dict = {}

    # creates a list from a string (again bc the previous list is contained in the scope of the previous func)
    words = file_contents.split()

    # loop ... for each word in the words list ...
    for word in words:
        # creates a new list where every capital letter is changed to to a small one
        lower_case_word = word.lower()

        # for each letter in the lower_case_letter list ...
        for letter in lower_case_word:

            # check to see if that char is not in the dict
            if letter not in charc_count_dict:
                # add that key and assign the value one to it
                charc_count_dict[letter] = 1
            # if it is ...
            else:
                # add one to the value of that key
                charc_count_dict[letter] += 1
    
    list_of_dicts = []

    for chars, count in charc_count_dict.items():
        new_dict = {"char": chars, "num": count}
        list_of_dicts.append(new_dict)

    def sort_chars(dictionary):
        return dictionary["num"]
    
    list_of_dicts.sort(reverse=True, key=sort_chars)
    for i in list_of_dicts:
        if i["char"].isalpha() == True:
            print(f"{i["char"]}: {i["num"]}")
    #sort_chars(charc_and_count)

    # returns the dict
    return list_of_dicts
#dictionary_of_chars_and_counts = charc_and_count(file_contents)


#def sort_chars (list_of_dicts):
 #   return list_of_dicts["num"]

'''
# the main func
def main():
    # creates a var called <file_contents>
    file_contents = get_book_text(path_to_file)

    # calls the <get_num_words> func ... that prints the num of words
    get_num_words(file_contents)
    # calls the <char_and_count> func ... that returns a dict
    #charc_and_count(file_contents)
'''
# calls main
#main()
