def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = char_count(text)
    print_report(book_path, text, chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def char_count(text):
    char_counts = {}
    
    for char in text:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        elif lower_char.isalpha():
            char_counts[lower_char] = 1

    def sort_on(dict):
        return dict["num"]

    char_list = [{"name": char, "num": count} for char, count in char_counts.items()]
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list

def print_report(path, text, dict):
    print(f"--- Begin report of {path} ---")
    word_count = get_num_words(text)
    print(f"{word_count} words found in the document")
    print("")
    char_report(dict)
    
def char_report(dict):
    for char in dict:
        name = char["name"]
        num = char["num"]
        print(f"The '{name}' character was found {num} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
