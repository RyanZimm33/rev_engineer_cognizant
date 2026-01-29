import pytest
from src.domain.book import Book
from src.services.book_service import BookService
from tests.mocks.mock_book_repository import MockBookRepo


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

def test_find_book_by_name_positive():
    query = "test"
    repo = MockBookRepo()
    svc = BookService(repo)

    book = svc.find_book_by_name(query)

    assert book[0].title == "test"
    assert book[0].author == "author"


def test_find_book_name_negative():
    name = 3
    repo = MockBookRepo()
    svc = BookService(repo)

    with pytest.raises(TypeError) as e:
        svc.find_book_by_name(name)
        assert str(e.value) == 'Expected str, got something else'

def test_add_book_positive():
    repo = MockBookRepo()
    svc = BookService(repo)
    book = Book(title="test", author="author")

    book_id = svc.add_book(book)

    assert book_id == "mock_id"

def test_add_book_negative():
    not_a_book = "book"
    repo = MockBookRepo()
    svc = BookService(repo)

    with pytest.raises(TypeError) as e:
        svc.add_book(not_a_book)
        assert str(e.value) == 'Expected Book, got something else'

def test_delete_book_positive():
    query = "book"
    repo = MockBookRepo()
    svc = BookService(repo)

    book_id = svc.delete_book(query)

    assert book_id == 'mock_id'

def test_delete_book_negative():
    query = 1
    repo = MockBookRepo()
    svc = BookService(repo)

    with pytest.raises(TypeError) as e:
        svc.delete_book(query)
        assert str(e.value) == 'Expected string, got something else'

def test_update_book_positive():
    query = "book"
    book = Book(title="test", author="author")
    repo = MockBookRepo()
    svc = BookService(repo)

    book_id = svc.update_book(query, book)

    assert book_id == 'mock_id'

def test_update_book_negative():
    query = "book"
    book = 2
    repo = MockBookRepo()
    svc = BookService(repo)

    with pytest.raises(TypeError) as e:
        svc.update_book(query, book)
        assert str(e.value) == 'Expected book, got something else'