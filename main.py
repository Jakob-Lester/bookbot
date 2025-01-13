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
    
    

    
        
def main():
    with open("books/frankenstein.txt") as f:
        f.contents = f.read()
        word_count = get_word_count(f.contents)
        character_count = get_character_count(f.contents)
        
        print([character_count])
        
    

main()
