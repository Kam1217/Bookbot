from stats import count_words, count_characters, sort_character_count
def get_book_text(filepath):
    with open(filepath) as book_file:
        return book_file.read()

#Print book words count to consol
def main():
    filepath = "./books/frankenstein.txt"
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_character_count = sort_character_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character_count in sorted_character_count:
        char = character_count["char"]
        num = character_count["num"]
        if char.isalpha():
            print(f"{char}: {num}")
            
main()