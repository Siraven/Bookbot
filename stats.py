def get_num_words(book):
    return len(book.split())

def get_letter_count(book):
    letter_count = {}
    for i in book:
        if i.lower() not in letter_count:
            letter_count[i.lower()] = 0
        letter_count[i.lower()] += 1
    return letter_count

def format_list(items):
    formatted_list = []
    for key, value in items.items():
        new_dict = {
            "char": key,
            "num": value
        }
        formatted_list.append(new_dict)
    return formatted_list


