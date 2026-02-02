import pytest
from src.domain.book import Book

def test_check_out_positive():
    book = Book(title="test", author="author", available=True, last_checkout="2030-01-28T17:45:41.055901")

    check_out_time = book.check_out()

    assert not book.available
    assert check_out_time == "2032-01-28T17:45:41.055901"


def test_check_out_negative():
    book = Book(title="test", author="author", available=False)

    with pytest.raises(Exception) as e: 
        book.check_out()
        assert str(e.value) == 'Book is already checked out.'

def test_check_in_positive():
    book = Book(title="test", author="author", available=False, last_checkout="2030-01-28T17:45:41.055901")

    check_in_time = book.check_in()

    assert book.available
    assert check_in_time == "2031-01-28T17:45:41.055901"


def test_check_in_negative():
    book = Book(title="test", author="author", available=True)

    with pytest.raises(Exception) as e: 
        book.check_in()
        assert str(e.value) == 'Book is already available.'   

def test_from_dict():
    dict_book = {"title" :"test", "author":"author"}
    book = Book.from_dict(dict_book)
    
    assert book.title == "test"
    assert book.author == "author"

def test_to_dict():
    book = Book(title="test", author="author")

    dict_book = book.to_dict()

    assert dict_book["title"] == "test"
    assert dict_book["author"] == "author"