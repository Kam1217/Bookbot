#Open and read book file
def get_book_text(filepath):
    with open(filepath) as book_file:
        return book_file.read()

#Print book file to consol
def main():
    print(get_book_text("./books/frankenstein.txt"))
    
main()