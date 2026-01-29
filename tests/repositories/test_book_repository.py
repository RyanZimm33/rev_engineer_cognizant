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

def test_delete_book():
    testing_file = "tests/test.json"
    repo = BookRepository(testing_file)
    
    book = Book(book_id= "to_delete",
    title= "to_delete",
    author= "to_delete",
    genre= "Fantasy",
    publication_year= 1945,
    page_count= 368,
    rating= 3.05,
    rating_count= 3109,
    price_usd= 70,
    publisher= "Blue River Books",
    language= "English",
    format= "Ebook",
    in_print= True,
    sales_millions= 3.54,
    last_checkout= "2026-01-27T10=32=53.493197",
    available= False
    )
    repo.add_book(book)
    book_id = repo.delete_book(book)

    assert book_id == "to_delete"