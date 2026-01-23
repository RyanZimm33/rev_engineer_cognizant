import json
import random
import uuid
from datetime import datetime, timedelta

def generate_books_json(filename = 'book.json', count = 500):
    genres = [
        'Fantasy',
        'Sci-Fi',
        'Non-Fiction',
        'Mystery',
        'Romance',
        'Technology',
        'History'
    ]

    publishers = [
        'North Star Press',
        'Emerald House',
        'Atlas Publishing',
        'Blue River Books'
    ]

    formats = [
        'Hardcover',
        'Paperback',
        'Ebook',
        'Audiobook'
    ]

    books = []

    for i in range(1, count + 1):                   #Generate a bunch of books, append to books list
        books.append( 
            {
                'book_id': str(uuid.uuid4()),
                'title': f'Book Title {i}',
                'author': f'Author: {random.randint(1, 80)}',
                'genre': random.choice(genres),
                'publication_year': random.randint(1850, 1950),
                'page_count': random.randint(120, 1100),
                'rating': round(random.uniform(1, 5), 2),
                'rating_count': random.randint(25, 10_000),
                'price_usd': round(random.uniform(7, 150), 2),
                'publisher': random.choice(publishers),
                'language': 'English',
                'format': random.choice(formats),
                'in_print': random.choice([True, True, True, True, False]),
                'sales_millions': round(random.uniform(.01, 15), 2),
                'last_checkout': datetime.now().isoformat() ,
                'available': random.choice([True, False])
            }
        )
    
    #Common json file manipulation methods
    #dump  - dumps to a file
    #dumps - dumps to a string
    #load  - load a filestream
    #loads - loads a string

    with open(filename, 'w', encoding='utf-8') as f:    #open filename as variable (f), w means writable
        json.dump(books, f, indent= 2)                  #Dump bookslist into file (f)
    
 
