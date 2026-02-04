import uuid
from datetime import datetime, timezone
from psycopg import Date
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, null
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.base import Base



class CheckoutHistory(Base):
    __tablename__ = "Checkout_history"

    checkout_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) #Sets column as dtype uuid, and as a primary key, and with a default value if none is provided

    book_id = Column(UUID(as_uuid=True), ForeignKey("books.book_id"), nullable=False) #Sets column as dtype uuid, as a foriegn key to the books table's pk book_id, cannot be null

    checkout_date = Column(DateTime, default=datetime.now(timezone.utc))
    return_date = Column(DateTime, nullable=True)
    due_date = Column(DateTime, nullable=True)
    returned = Column(Boolean, default=False)

    book = relationship("Book", backref="checkout_records") #Provides acesss to book.checkout_records easily, we could do [c for c in book.checkout_records if not c.returned]