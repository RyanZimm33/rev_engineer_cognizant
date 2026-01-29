from src.repositories.book_repository import BookRepository
from src.services.book_generator_service import generate_books_json
from src.domain.book import Book
from src.services.book_analytics_service import BookAnalyticsService
from src.services.book_service import BookService
import requests

class BookREPL:
    def __init__(self, book_service, book_analytics_service):
        self.running = True
        self.book_service = book_service
        self.book_analytics_service = book_analytics_service

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
            print("Available commands: addBook, getAllRecords, updateBook, deleteBook, findByName, getJoke, getAveragePrice, getTopBooks, getValueScores, getMedianPriceByGenre, getMostPopularGenre2026, help, exit")
        elif cmd == 'addBook':
            self.add_book()
        elif cmd == 'getAllRecords':
            self.get_all_records()
        elif cmd == 'updateBook':
            self.update_book()
        elif cmd == 'deleteBook':
            self.delete_book()
        elif cmd == 'findByName':
            self.find_book_by_name()
        elif cmd == 'getJoke':
            self.get_joke()
        elif cmd == "getAveragePrice":
            self.get_average_price()
        elif cmd == "getTopBooks":
            self.get_top_books()
        elif cmd == "getValueScores":
            self.get_value_scores()
        elif cmd == "getMedianPriceByGenre":
            self.get_median_price_by_genre()
        elif cmd == "getMostPopularGenre2026":
            self.get_most_popular_genre_2026()
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
    
    def get_average_price(self):
        try:
            books = self.book_service.get_all_books()
            avg_price = self.book_analytics_service.average_price(books)
            print(avg_price)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')

    def get_top_books(self):
        try:
            books = self.book_service.get_all_books()
            top_books = self.book_analytics_service.top_rated(books)
            print(top_books)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')

    def get_value_scores(self):
        try:
            books = self.book_service.get_all_books()
            value_scores = self.book_analytics_service.value_scores(books)
            print(value_scores)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')
    
    def get_median_price_by_genre(self):
        try:
            books = self.book_service.get_all_books()
            median_prices = self.book_analytics_service.median_price_by_genre(books)
            print(median_prices)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')
    
    def get_most_popular_genre_2026(self):
        try:
            books = self.book_service.get_all_books()
            most_popular = self.book_analytics_service.most_popular_genre_2026(books)
            print(most_popular)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')
    
    def delete_book(self):
        try:
            query = input('Please enter the name of the book to delete: ')
            deleted_book_id = self.book_service.delete_book(query)
            print(deleted_book_id)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')
        
    def update_book(self):
        try:
            query = input('Please enter the name of the book to update: ')
            print("Enter Book Details")
            title = input('Title: ')
            author = input('Author: ')
            book = Book(title= title, author=author)
            updated_book_id = self.book_service.update_book(query, book)
            print(updated_book_id)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')

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
        try:
            query = input('Please enter book name: ')
            books = self.book_service.find_book_by_name(query)
            print(books)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')

if __name__ == '__main__':
    generate_books_json()
    repo = BookRepository('book.json')
    book_srv = BookService(repo)
    book_analytics_srv = BookAnalyticsService()
    repl = BookREPL(book_srv, book_analytics_srv)
    repl.start()

