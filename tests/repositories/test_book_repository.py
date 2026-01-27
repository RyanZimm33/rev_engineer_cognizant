import pytest
from src.domain.book import Book
from src.repositories.book_repository import BookRepository

def test_get_all_books():
    testing_file = "tests/test.json"
    repo = BookRepository(testing_file)

    books = repo.get_all_books()

    assert books[0].title == "test"
    assert books[1].title == "test2"

def test_add_book():
    testing_file = "tests/test.json"
    repo = BookRepository(testing_file)
    book = Book(book_id="test3", title="test3", author="test")

    book_id = repo.add_book(book)

    assert book_id == "test3"

def test_find_book_by_name():
    testing_file = "tests/test.json"
    repo = BookRepository(testing_file)
    query = "test"

    books = repo.find_book_by_name(query)

    assert books[0].title == "test"