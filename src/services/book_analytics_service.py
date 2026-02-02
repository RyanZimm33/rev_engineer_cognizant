import numpy as np
from src.domain.book import Book

class BookAnalyticsService:
    def average_price(self, books : list[Book]) -> float:
        if not isinstance(books, list) or not all(isinstance(b, Book) for b in books):
            raise TypeError('Expected a Book list, got something else')
        prices = np.array([b.price_usd for b in books], dtype = float)  #Create array of book prices for all books
        return prices.mean()
    
    def top_rated(self, books: list[Book], min_ratings: int = 1000, limit: int = 10) -> list[Book]:  #Return a list of books of size limit with the highest average rating and a ratings_count of atleast min_ratings
        if not isinstance(books, list) or not all(isinstance(b, Book) for b in books):
            raise TypeError('Expected a Book list, got something else')
        if not (isinstance(min_ratings, int) or isinstance(limit, int)):
            raise TypeError('Expected an int, got something else')
         
         
        ratings = np.array([b.rating for b in books])    #nparray of the average_rating of all books
        counts = np.array([b.rating_count for b in books])     #nparray of the ratings_count of all books

        #Filtered books contains all books that have atleast min_ratings
        mask = counts >= min_ratings             #Mask that is true for all books that have atleast min_ratings
        filteredBooks = np.array(books)[mask]    #Filter books by the mask
        scores = ratings[mask]                   #Filter ratings by the mask, i.e. this is only the ratings for the filtered books
        sorted_idx = np.argsort(scores)[::-1]    #Creates an index, a list of all the indexs of where the filteredBooks should go to be sorted by scores
        return filteredBooks[sorted_idx].tolist()[:limit] #Return list of filtered and sorted books up to limit

    def value_scores(self, books: list[Book]) -> dict[str, float]:
        if not isinstance(books, list) or not all(isinstance(b, Book) for b in books):
            raise TypeError('Expected a Book list, got something else')
        ratings = np.array([b.rating for b in books])    
        counts = np.array([b.rating_count for b in books])     
        prices = np.array([b.price_usd for b in books])

        scores = (ratings * np.log1p(counts)) / prices    #for each element in ratings,count and prices; multiply and divided and creat new nparray with result for each
        
        #Dicitionary comprehension to format data
        return {
            book.book_id: float(score)
            for book, score in zip(books, scores)      #Iterate over books and scores in parralel, add the book.bookid and score to the dictionary
        }

    def median_price_by_genre(self, books: list[Book]) -> dict[str, float]:
        if not isinstance(books, list) or not all(isinstance(b, Book) for b in books):
            raise TypeError('Expected a Book list, got something else')
        book_prices = np.array([b.price_usd for b in books])
        book_genres = np.array([b.genre for b in books])
        unique_genres = np.unique(book_genres)

        genre_medians = {}
        for genre in unique_genres:
            mask = book_genres == genre
            genre_filtered_book_prices = np.array(book_prices)[mask]
            genre_medians[genre] = np.median(genre_filtered_book_prices)
        
        return genre_medians
    
    def most_popular_genres_2026(self, books: list[Book]) -> dict[str, int]:
        if not isinstance(books, list) or not all(isinstance(b, Book) for b in books):
            raise TypeError('Expected a Book list, got something else')
        book_genres = np.array([b.genre for b in books])
        book_date = np.array([b.publication_year for b in books])
        mask = book_date == 2026
        unique_genres, counts = np.unique(book_genres[mask], return_counts=True)

        return dict(zip(unique_genres, counts))


