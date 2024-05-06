def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    char_dict = character_count(text)
    sort = sort_dict(char_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words were found in this document")
    create_report(sort)
    print("--- End report ---")
def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    character_dict = {}
    lower_cased = text.lower()
    for character in lower_cased:
        if character.isalpha():
            if character in character_dict:
                character_dict[character] = character_dict[character] + 1
            else:
                 character_dict[character] = 1
    return character_dict

def sort_dict(character_dict):
    character_list = [(char,count) for char, count in character_dict.items()]
    sorted_list = sorted(character_list, key=lambda item: item[1], reverse=True)
    return sorted_list
def create_report(sorted_list):
    for char, count in sorted_list:
        print(f"The '{char} character was found {count}")
    

         
    
main()
