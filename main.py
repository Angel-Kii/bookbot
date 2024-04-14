def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = dict_to_list(get_num_letters(text))
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for each in num_letters:
        print(f"The '{each["letter"]}' character was found {each["num"]} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    letter_count = {}
    for letter in text:
        letter = letter.lower()
        if not letter.isalpha():
            continue
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def sort_on(dict):
    return dict['num']

def dict_to_list(dict):
    list = []
    for each in dict:
        new_dict = {"letter":each,"num":dict[each]}
        list.append(new_dict)
    list.sort(reverse=True,key=sort_on)
    return list

main()