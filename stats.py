# Given filepath, return contents as stirng
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# Given string, return integer representing number of total words
def get_num_words(string):
    split_words = string.split()
    return len(split_words)

# Given a string, return a dict showing total uses of each unique character
def get_num_characters(string):
    string = string.lower() # Set to lower to prevent duplicates
    char_dict = {}
    for char in string:
        if char in char_dict:
            # char exists, increment
            char_dict[char] += 1
        else:
            # doesnt exist, create
            char_dict[char] = 1
    if " " in char_dict:
        del char_dict[" "]
    return char_dict

def sort_on(items):
    return items["num"]

# Given a dictionary of chars, sort by num
def sort_dict(char_dict):
    sorted_list = []
    for char, num in char_dict.items():
        sorted_list.append({"char": char, "num": num})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    