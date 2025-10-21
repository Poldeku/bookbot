def get_num_words(text):
    words_count = len(text.split())
    return f"Found {words_count} total words"

def get_num_chars(text):
    char_num = {}
    for chr in list(text.lower()):
        if chr not in char_num:
            char_num[chr] = 1
        else:
            char_num[chr] += 1
    return char_num

def sort_on(items):
    return items["num"]

def sort_dict(dictionary):
    dict_list = []
    for key, value in dictionary.items():
        new_dict = {
            "char": key,
            "num": value
        }
        dict_list.append(new_dict) 
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list