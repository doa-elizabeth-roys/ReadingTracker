
def display_menu():
    print("Menu:")
    print("L - List all books")
    print("A - Add new book")
    print("M - Mark a book as completed")
    print("Q - Quit")


def read_book():
    for i, book in enumerate(book_details):
        title, author, pages, status = book.split(",")
        if status == "r":
            print(f"*{i + 1}. {title} by {author} {pages} pages")
        else:
            print(f"{i + 1}. {title} by {author} {pages} pages")


def add_book():
    title = ""
    while title == "":
        title = input("Title: ")
        if title == "":
            print("Input cannot be blank.")

    author = ""
    while author == "":
        author = input("Author: ")
        if author == "":
            print("Input cannot be blank.")

    pages = 0
    while pages <= 0:
        try:
            pages = int(input("Pages: "))
            if pages <= 0:
                print("Pages must be greater than 0.")
        except ValueError:
            print("Invalid input; enter a valid number.")

    print(f"{title} by {author}, ({pages} pages) added to Reading Tracker")
    book_file.writelines(f"*{title}, {author}, {pages}")
    display_menu()

# def quit_tracker():



print("Reading Tracker 1.0 - by Doa Roys")
book_file = open("books.csv", "r")
book_details = book_file.readlines()
book_file.close()
print("Loaded", len(book_details), "books")
display_menu()
user_choice = input("")
if user_choice.upper() == "L":
    read_book()
elif user_choice.upper() == "A":
    add_book()
# elif user_choice.upper() == "Q":
#     quit_tracker()