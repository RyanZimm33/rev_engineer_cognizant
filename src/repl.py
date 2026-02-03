from src.repositories.book_repository import BookRepository
from src.repositories.checkout_history_repository import CheckoutHistoryRepository
from src.domain.book import Book
from src.domain.checkout_history import CheckoutHistory
from src.services.book_analytics_service import BookAnalyticsService
from src.services.book_service import BookService
from src.services.checkout_history_service import CheckoutHistoryService
from src.services.chart_service import ChartService
import requests
import uuid

class BookREPL:
    def __init__(self, book_service, book_analytics_service, checkout_history_service, chart_service):
        self.running = True
        self.book_service = book_service
        self.book_analytics_service = book_analytics_service
        self.checkout_history_service = checkout_history_service
        self.chart_service = chart_service

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
            print("           Basic:    addBook, getAllRecords, updateBook, deleteBook, findByName, getJoke") 
            print("       Analytics:    getAveragePrice, getTopBooks, getValueScores, getMedianPriceByGenre" )
            print(" Chart Analytics:    mostPopularGenres2026, highestRatedGenres, ratingVsPrice, releasesByYear, availableVsUnavailable" )
            print("Checkout History:    checkIn, checkOut, getAllCheckoutHistory, getBookCheckoutHistory")
            print("             App:    help, exit")
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
        elif cmd == "mostPopularGenres2026":
            self.get_most_popular_genres_2026()
        elif cmd == "highestRatedGenres":
            self.get_highest_rated_genres()
        elif cmd == "ratingVsPrice":
            self.get_rating_vs_price()
        elif cmd == "releasesByYear":
            pass
        elif cmd == "availableVsUnavailable":
            pass
        elif cmd == "checkIn":
            self.check_in()
        elif cmd == "checkOut":
            self.check_out()
        elif cmd == "getAllCheckoutHistory":
            self.get_all_checkout_history()
        elif cmd == "getBookCheckoutHistory":
            self.get_book_checkout_history()
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
    
    def get_most_popular_genres_2026(self):
        try:
            books = self.book_service.get_all_books()
            data = self.book_analytics_service.most_popular_genres_2026(books)
            self.chart_service.bar_chart("Genres", "Number Published", data)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')
    
    def get_highest_rated_genres(self):
        try:
            books = self.book_service.get_all_books()
            data = self.book_analytics_service.highest_rated_genres(books)
            self.chart_service.bar_chart("Genres", "Ratings", data)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')
    
    def get_rating_vs_price(self):
        try:
            books = self.book_service.get_all_books()
            data = self.book_analytics_service.rating_vs_price(books)
            self.chart_service.scatter_chart("Price", "Ratings", data)
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
            book_id = book_id=str(uuid.uuid4())
            book = Book(book_id= book_id, title= title, author= author)
            new_book_id = self.book_service.add_book(book)
            history = CheckoutHistory(book_id= book_id, check_out= book.check_out)
            self.checkout_history_service.add_checkout_history(history)
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

    def check_in(self):
        try:
            query = input('Please enter book name: ')
            book = self.book_service.find_book_by_name(query)[0]
            check_in_time = book.check_in()
            self.book_service.update_book(query, book)
            history = CheckoutHistory(book_id= book.book_id, check_in= check_in_time)
            self.checkout_history_service.add_checkout_history(history)
            print(check_in_time)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')
    
    def check_out(self):
        try:
            query = input('Please enter book name: ')
            book = self.book_service.find_book_by_name(query)[0]
            check_out_time = book.check_out()
            self.book_service.update_book(query, book)
            history = CheckoutHistory(book_id= book.book_id, check_out= check_out_time)
            self.checkout_history_service.add_checkout_history(history)
            print(check_out_time)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')

    def get_all_checkout_history(self):
        history = self.checkout_history_service.get_all_checkout_history()
        print(history)

    def get_book_checkout_history(self):
        try:
            query = input('Please enter book name: ')
            book = self.book_service.find_book_by_name(query)[0]
            history = self.checkout_history_service.find_checkout_history_by_book_id(book.book_id)
            print(history)
        except Exception as e:
            print(f'An unexpected error has occurred {e}')


if __name__ == '__main__':
    book_repo = BookRepository('book.json')
    checkout_history_repo = CheckoutHistoryRepository('checkout_history.json')
    book_srv = BookService(book_repo)
    book_analytics_srv = BookAnalyticsService()
    checkout_history_srv = CheckoutHistoryService(checkout_history_repo)
    chart_srv = ChartService()
    repl = BookREPL(book_srv, book_analytics_srv, checkout_history_srv, chart_srv)
    repl.start()

