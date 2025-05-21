def get_book_text(filepath):
    with open(filepath) as book_file:
        return book_file.read()

def main():
    print(get_book_text("./books/frankenstein.txt"))
    

main()