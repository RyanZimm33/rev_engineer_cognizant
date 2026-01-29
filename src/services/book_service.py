from doctest import REPORT_CDIFF

from httpx import delete
from src.repositories.book_repository_protocol import BookRepositoryProtocol
from src.domain.book import Book

class BookService:
    def __init__(self, repo: BookRepositoryProtocol):
        self.repo = repo

    def get_all_books(self) -> list[Book]:
        return self.repo.get_all_books()
    
    def add_book(self, book:Book) -> str:
        if not isinstance(book, Book):
            raise TypeError('Expected Book, got something else')
        return self.repo.add_book(book)
    
    def find_book_by_name(self, query:str) -> list[Book]:
        if not isinstance(query, str):
            raise TypeError('Expected String, got something else')
        return self.repo.find_book_by_name(query)
    
    def delete_book(self, query:str) -> str | None:
        if not isinstance(query, str):
            raise TypeError('Expected String, got something else')
        books = self.find_book_by_name(query)
        if len(books) > 0:
            return self.repo.delete_book(books[0])
    
    def update_book(self, query:str, book:Book) -> str | None:
        if not isinstance(query, str):
            raise TypeError('Expected String, got something else')
        if not isinstance(book, Book):
            raise TypeError('Expected Book, got something else')
        old_book_id = self.delete_book(query)
        if old_book_id: 
            book.book_id = old_book_id
            self.repo.add_book(book)
            return old_book_id