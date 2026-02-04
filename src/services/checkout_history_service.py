from src.domain.checkout_history import CheckoutHistory
from src.repositories.checkout_history_repository_protocol import CheckoutHistoryRepositoryProtocol

class CheckoutHistoryService:
    def __init__(self, repo: CheckoutHistoryRepositoryProtocol):
        self.repo = repo
    
    def get_all_checkout_history(self) -> list[CheckoutHistory]:
        return self.repo.get_all_checkout_history()

    def find_checkout_history_by_book_id(self, book_id:str) -> list[CheckoutHistory]:
        if not isinstance(book_id, str):
            raise TypeError('Expected String, got something else')
        return self.repo.find_checkout_history_by_book_id(book_id)

    def add_checkout_history(self, history:CheckoutHistory) -> str:
        if not isinstance(history, CheckoutHistory):
            raise TypeError('Expected Checkout History, got something else')
        return self.repo.add_checkout_history(history)