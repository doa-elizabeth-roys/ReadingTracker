print("Reading Tracker 1.0 - by Doa Roys")
book_file = open("books.csv", "r")
book_details = book_file.readlines()
book_file.close()
print("Loaded", len(book_details), "books")

def display_menu():
    print("Menu:")
    print("L - List all books")
    print("A - Add new book")
    print("M - Mark a book as completed")
    print("Q - Quit")


def read_book():
    global book_details
    book_file = open("books.csv", "r")
    book_details = book_file.readlines()
    book_file.close()

    for i, book in enumerate(book_details):
        book = book.strip()  # Remove leading/trailing whitespace
        values = book.split(",")

        # Check if the line has enough values
        if len(values) == 4:
            title, author, pages, status = values
            if status == "r":
                print(f"*{i + 1}. {title} by {author} {pages} pages")
            else:
                print(f"{i + 1}. {title} by {author} {pages} pages")
        else:
            print(f"Error: Invalid book details on line {i + 1}.")

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
    # book_file = open("books.csv","w")
    # book_file.close()
    # Add book to book_details list in memory
    book_details.append(f"{title}, {author}, {pages},r\n")
    display_menu()
    user_choice = input("")

def quit_tracker():
    book_file = open("books.csv", "r")
    book_details = book_file.readlines()
    book_file.close()
    print(f" {len(book_details)} books saved to books.csv")
    print("So many books, so little time. Frank Zappa")
def mark_book():
    # global pages_to_read, book_details
    read_book()
    pages_to_read: int = 0
    book_to_read: int = 1
    for book in book_details:
        title, author, pages, status = book.split(",")
        if status == "r":
            pages_to_read += int(pages) #sum(int(book.split(",")[2])
            book_to_read = book_to_read + 1
    if pages_to_read == 0:
        print("No required books!")
        return
    print(f"You need to read {pages_to_read} pages to read in {book_to_read} books")
    # for i, book in enumerate(book_details):
    #     title, author, pages, status = book.split(",")
    while True:
        try:
            book_no = int(input("Enter the number of a book to mark as completed: "))
            if book_no <= 0:
                print("Number must be greater than 0")
            elif book_no > len(book_details):
                print("Invalid book number")
            else:
                title, author, pages, status = book_details[book_no - 1].split(",")
                if status == "c":
                    print("That book is already completed")
                else:
                    book_details[book_no - 1] = f"{title},{author},{pages},c"
                    print(f"{title} by {author} marked as completed")
                    display_menu()
                    break
        except ValueError:
            print("Invalid input; enter a valid number")





display_menu()
user_choice = input("")
if user_choice.upper() == "L":
    read_book()
elif user_choice.upper() == "A":
    add_book()
elif user_choice.upper() == "Q":
    quit_tracker()
elif user_choice.upper() == "M":
    mark_book()