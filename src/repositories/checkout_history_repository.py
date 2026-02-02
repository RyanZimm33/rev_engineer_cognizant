import json
from src.domain.checkout_history import CheckoutHistory
from src.repositories.checkout_history_repository_protocol import CheckoutHistoryRepositoryProtocol

class CheckoutHistoryRepository(CheckoutHistoryRepositoryProtocol):
    def __init__(self, filepath: str="checkout_history.json"):
        self.filepath = filepath

    def get_all_checkout_history(self) -> list[CheckoutHistory]:
        with open(self.filepath, 'r', encoding='utf8') as f:  
            data = json.load(f)
            return [CheckoutHistory.from_dict(item) for item in data]
    
    def add_checkout_history(self, history:CheckoutHistory) -> str:
        checkout_history = self.get_all_checkout_history()
        checkout_history.append(history)
        with open(self.filepath, 'w', encoding='utf-8') as f:       
            json.dump([c.to_dict() for c in checkout_history], f, indent=2)  
        return history.book_id
    
    def find_checkout_history_by_book_id(self, book_id:str) -> list[CheckoutHistory]:
        checkout_history = self.get_all_checkout_history()
        return [c for c in checkout_history if c.book_id == book_id]
