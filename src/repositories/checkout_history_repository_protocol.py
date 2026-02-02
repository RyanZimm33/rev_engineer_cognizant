from typing import Protocol
from src.domain.checkout_history import CheckoutHistory

class CheckoutHistoryRepositoryProtocol(Protocol):
    def get_all_checkout_history(self) -> list[CheckoutHistory]:
        ...
    
    def add_checkout_history(self, history:CheckoutHistory) -> str:
        ...
    
    def find_checkout_history_by_book_id(self, book_id:str) -> list[CheckoutHistory]:
        ...