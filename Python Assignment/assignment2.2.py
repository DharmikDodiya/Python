from tabulate import tabulate

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1  # To generate unique book ids

    # Add a book to the library
    def addBook(self, title, author):
        book = Book(self.next_id, title, author)
        self.books.append(book)
        self.next_id += 1  # Increment the ID for the next book

    # Remove a book from the library by its ID
    def removeBook(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book with ID: {book_id} has been removed.\n")
                return
        print(f"Book with ID: {book_id} not found.\n")

    # Search for books by title
    def searchBookByTitle(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]

        if not found_books:
            print(f"No books found with the title: {title}.\n")
            return []

        return found_books

    # Display all books in the library in tabular format
    def listBooks(self):
        if not self.books:
            print("No books in the library.\n")
            return

        book_list = [(book.book_id, book.title, book.author) for book in self.books]
        print(tabulate(book_list, headers=["ID", "Title", "Author"], tablefmt="grid"))


# Example usage
library = Library()

# Static 3 books to display initially
library.addBook("The Great Gatsby", "F. Scott Fitzgerald")
library.addBook("To Kill a Mockingbird", "Harper Lee")
library.addBook("1984", "George Orwell")

# Display static data initially
print("Initial Library Data:")
library.listBooks()

# Main loop for user interaction
while True:
    print("\nOptions:")
    print("1. Add a Book")
    print("2. Remove a Book by ID")
    print("3. Search Books by Title")
    print("4. Show All Books")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        # Add a book
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        library.addBook(title, author)
        print("Book added successfully.\n")

    elif choice == '2':
        # Remove a book by ID
        library.listBooks()  # Show current books before asking for ID
        try:
            book_id = int(input("Enter the ID of the book to remove: "))
            library.removeBook(book_id)
        except ValueError:
            print("Invalid input. Please enter a valid book ID.\n")

    elif choice == '3':
        # Search books by title
        title = input("Enter a title to search for: ")
        search_results = library.searchBookByTitle(title)
        if search_results:
            print(f"Search results for '{title}':")
            book_list = [(book.book_id, book.title, book.author) for book in search_results]
            print(tabulate(book_list, headers=["ID", "Title", "Author"], tablefmt="grid"))

    elif choice == '4':
        # Show all books
        print("Current Library Data:")
        library.listBooks()

    elif choice == '5':
        # Exit
        print("Exiting the library system.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
