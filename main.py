def get_word_count(book):
    words = book.split()
    word_counter = 0
    for word in words:
        word_counter += 1
    return word_counter

def get_character_count(book):
    lowered_words = book.lower()
    words = lowered_words.split()
    used_chars = {}
    for word in words:     
        for char in word:     
            if char in used_chars:
                used_chars[char] += 1
            else:
                used_chars[char] = 1
    return used_chars

def sort_dict(dict):
    keys = []
    vals = []
    new_dict = {}
    for key in dict:
        if key.isalpha() == True:
            keys.append(key)
            vals.append(dict[key])
            
    for key in keys:
        for val in vals:
            new_dict[key] = val
            vals.remove(val)
            break
    
    val_ordered = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[1], reverse=True)}
    return val_ordered
        
def main():
    with open("books/frankenstein.txt") as f:
        f.contents = f.read()
        word_count = get_word_count(f.contents)
        character_count = get_character_count(f.contents)
        ordered_dict = sort_dict(character_count)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        for key in ordered_dict:
            print(f"The '{key}' character was found {ordered_dict[key]} times")
        print("--- End report ---")


main()
