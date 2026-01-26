import pytest
from src.domain.book import Book
from src.services.book_service import BookService
from tests.mocks.mock_book_repository import MockBookRepo

#Positive Test: Give correct data, check for correct output
def test_get_all_books_positive():
    # AAA - arrange, act, assert

    #Arrange
    repo = MockBookRepo()
    svc = BookService(repo)

    #Act
    books = svc.get_all_books()

    #Assert
    assert len(books) == 1
    assert books[0].title == "test"
    assert books[0].author == "author"

#Negative Test: Give incorrect data, ensure it is handled gracefully
def test_find_book_name_negative():
    name = 3
    repo = MockBookRepo()
    svc = BookService(repo)

    with pytest.raises(TypeError) as e:
        svc.find_book_by_name(name)
        assert str(e.value) == 'Expected str, got something else'

def test_add_book():
    repo = MockBookRepo()
    svc = BookService(repo)
    book = Book(title="test", author="author")

    book_id = svc.add_book(book)

    assert book_id == "mock_id"

def test_find_book_by_name():
    query = "test"
    repo = MockBookRepo()
    svc = BookService(repo)

    book = svc.find_book_by_name(query)

    assert book[0].title == "test"
    assert book[0].author == "author"