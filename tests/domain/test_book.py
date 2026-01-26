from ast import Dict
import pytest
from src.domain.book import *

def test_check_out_positive():
    book = Book(title="test", author="author", available=True)

    book.check_out()

    assert not book.available


def test_check_out_negative():
    book = Book(title="test", author="author", available=False)

    with pytest.raises(Exception) as e: 
        book.check_out()
        assert str(e.value) == 'Book is already checked out.'

def test_check_in_positive():
    book = Book(title="test", author="author", available=False)

    book.check_in()

    assert book.available


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