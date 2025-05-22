from stats import count_words , count_characters

#Open and read book file
def get_book_text(filepath):
    with open(filepath) as book_file:
        return book_file.read()

#Print book words count to consol
def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    print(f"{word_count} words found in the document")
    print(character_count)

main()