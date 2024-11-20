print("Reading Tracker 1.0 - by Doa Roys")
book_file = open("books.csv", "r")
book_details = book_file.readlines()
book_file.close()
print("Loaded", len(book_details), "books")

print("Menu:")
print("L - List all books")
print("A - Add new book")
print("M - Mark a book as completed")
print("Q - Quit")


def read_book():

    for i, book in enumerate(book_details):
        title, author, pages, status = book.split(",")
        if status == "r":
            print(f"*{i+1}. {title} by {author} {pages} pages")
        else:
            print(f"{i+1}. {title} by {author} {pages} pages")


user_choice = input("")
if user_choice.upper() == "L":
    read_book()
