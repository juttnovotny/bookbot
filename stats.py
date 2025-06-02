
def get_num_words(book_string):
    # takes a string and returns a list of words
    word_list = book_string.split()
    return len(word_list)

def get_char_count(book_string):
    # take a string and return a dictionary of chars:count(int)
    lowercase_string = book_string.lower()
    char_dict = {}
    for char in lowercase_string:
        if char_dict.get(char) == None:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def get_sorted_list(dictionary):
    initial_list = []
    for entry in dictionary:
        temp_dict = {"char": entry, "num": dictionary.get(entry)}
        initial_list.append(temp_dict)
    sorted_list = sorted(initial_list, key=lambda x: x["num"])
    return sorted_list
    