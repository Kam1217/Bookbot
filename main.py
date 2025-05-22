#Open and read book file
def get_book_text(filepath):
    with open(filepath) as book_file:
        return book_file.read()

#Count number of words
def count_words(text):
    word_count = len(text.split())
    return word_count
    
#Print book words count to consol
def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")

main()