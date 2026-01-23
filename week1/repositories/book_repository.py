import json
from week1.domain.book import Book
from week1.repositories.book_repository_protocol import BookRepositoryProtocol

class BookRepository(BookRepositoryProtocol):
    def __init__(self, filepath: str="books.json"):
        self.filepath = filepath
    
    def get_all_books(self) -> list[Book]:
        with open(self.filepath, 'r', encoding='utf8') as f:    #Open file as readable
            data = json.load(f)
            return [Book.from_dict(item) for item in data]
    
    def add_book(self, book:Book) -> str:
        books = self.get_all_books()
        books.append(book)
        with open(self.filepath, 'w', encoding='utf-8') as f:       #Open file as wrightable
            json.dump([b.to_dict() for b in books], f, indent=2)    #Convert Book datatype to json serializable type via list comprehension
        return book.book_id
    
    def find_book_by_name(self, query) -> list[Book]:
        books = self.get_all_books()
        return [b for b in books if b.title == query]
