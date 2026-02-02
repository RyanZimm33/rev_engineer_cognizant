from src.domain.checkout_history import CheckoutHistory

class MockCheckoutHistoryRepo:
    def get_all_checkout_history(self) -> list[CheckoutHistory]:
        return [CheckoutHistory(book_id="test", check_in="2020")]
    
    def add_checkout_history(self, history:CheckoutHistory) -> str:
        return history.book_id

    def find_checkout_history_by_book_id(self, book_id:str) -> list[CheckoutHistory]:
        return [CheckoutHistory(book_id=book_id, check_in="2020")]