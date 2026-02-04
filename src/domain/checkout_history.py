from typing import Optional
from dataclasses import dataclass

@dataclass
class CheckoutHistory():
    book_id : str
    check_out : Optional[str] = None
    check_in : Optional[str] = None
   
    def get_time(self) -> list[str]:
        if self.check_out:
            return ["check_out", self.check_out]
        else:
            return ["check_in", self.check_in]

    @classmethod
    def from_dict(cls, data:dict) -> 'CheckoutHistory':     #Match dictionary data to checkout history class
        return cls(**data)
    
    def to_dict(self) -> dict:
        time = self.get_time()
        return {
            "book_id": self.book_id,
            time[0]:time[1]
        }
    
