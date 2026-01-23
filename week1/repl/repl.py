from week1.repositories.book_repository import BookRepository
from week1.services.book_generator_service import generate_books_json
from week1.domain.book import Book
from week1.services.book_service import BookService

class BookREPL:
    def __init__(self, book_service):
        self.running = True
        self.book_service = book_service

    def start(self):
        print("Welcome to the Book App, type help for command list")
        while self.running:
            cmd = input('>>>').strip()
            self.handle_command(cmd)

    def handle_command(self, cmd):
        if cmd == 'exit':
            self.running = False
            print("Goodbye.")
        elif cmd == 'help':
            print("Available commands: addBook, getAllRecords, findByName, help, exit")
        elif cmd == 'addBook':
            self.add_book()
        elif cmd == 'getAllRecords':
            self.get_all_records()
        elif cmd == 'findByName':
            self.find_book_by_name()
        else:
            print("Invalid Command")


    def get_all_records(self):
        books = self.book_service.get_all_books()
        print(books)

    def add_book(self):
        try:
            print("Enter Book Details")
            title = input('Title: ')
            author = input('Author: ')
            book = Book(title= title, author=author)
            new_book_id = self.book_service.add_book(book)
            print(new_book_id)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')
    
    def find_book_by_name(self):
        query = input('Please enter book name: ')
        books = self.book_service.find_book_by_name(query)
        print(books)

if __name__ == '__main__':
    generate_books_json()
    repo = BookRepository('book.json')
    book_srv = BookService(repo)
    repl = BookREPL(book_srv)
    repl.start()

