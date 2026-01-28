import pytest
from src.domain.book import Book
from src.services.book_analytics_service import BookAnalyticsService
from tests.mocks.mock_book_repository import MockBookRepo

def test_average_price():
    books = [Book(title = "test", author = "author", price_usd=10)]
    srv = BookAnalyticsService()

    price = srv.average_price(books)

    assert price == 10


def test_top_rated():
    books = [Book(title = "test", author = "author", rating= 1, rating_count=2000), 
             Book(title = "test2", author = "author", rating=0, rating_count=2000)]
    srv = BookAnalyticsService()

    top_books = srv.top_rated(books)

    assert len(top_books) == 2
    assert top_books[0].title == "test"
    assert top_books[1].title == "test2"

def test_value_scores():
    books = [Book(book_id= "test", title = "test", author = "author", rating= 1, rating_count=1000, price_usd=50), 
             Book(book_id= "test2", title = "test",  author = "author", rating=.8, rating_count=2000, price_usd=60)]
    srv = BookAnalyticsService()

    book_values = srv.value_scores(books).keys()

    assert len(book_values) == 2

def test_median_price_by_genre():
    genres = ["Fantasy", "History"]
    books = [Book(title= "test", author = "test", genre="History", price_usd=50), 
             Book(title= "test2",author = "test", genre="History", price_usd=51), 
             Book(title= "test3", author = "test", genre="Fantasy", price_usd=50)]
    srv = BookAnalyticsService()

    median_prices = srv.median_price_by_genre(books, genres)

    assert len(median_prices) == 2
    assert median_prices["Fantasy"] == 50.0
    assert median_prices["History"] == 50.5

def test_most_popular_genre_2026():
    books = [Book(title= "test", author = "test", genre="History", price_usd=50, last_checkout="2025"), 
             Book(title= "test2",author = "test", genre="History", price_usd=51, last_checkout="2025"), 
             Book(title= "test3", author = "test", genre="Fantasy", price_usd=50, last_checkout="2026")]
    srv = BookAnalyticsService()

    popular_genre = srv.most_popular_genre_2026(books)

    assert popular_genre == "Fantasy: 1"
    