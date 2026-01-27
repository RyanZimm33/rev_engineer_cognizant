from src.repositories.book_repository import BookRepository
from src.services.book_generator_service import generate_books_json
from src.domain.book import Book
from src.services.book_service import BookService
import requests

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
        elif cmd == 'getJoke':
            self.get_joke()
        else:
            print("Invalid Command")

    def get_joke(self):
        try:
            url = 'https://api.chucknorris.io/jokes/random'
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            print(response.json()['value'])
        except requests.exceptions.Timeout:
            print('Request timed out.')
        except requests.exceptions.HTTPError as e:
            print(f'HTTP Error: {e}')
        except requests.exceptions.RequestException as e:
            print(f'Something else went wrong: {e}')
    
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

