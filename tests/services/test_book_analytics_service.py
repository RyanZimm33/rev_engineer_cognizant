from matplotlib.style import available
import pytest
from src.domain.book import Book
from src.services.book_analytics_service import BookAnalyticsService

def test_average_price_positive():
    books = [Book(title = "test", author = "author", price_usd=10)]
    srv = BookAnalyticsService()

    price = srv.average_price(books)

    assert price == 10

def test_average_price_negative():
    books = [1,2]
    svc = BookAnalyticsService()

    with pytest.raises(TypeError) as e:
        svc.average_price(books)
        assert str(e.value) == 'Expected a Book list, got something else'

def test_top_rated_positive():
    books = [Book(title = "test", author = "author", rating= 1, rating_count=2000), 
             Book(title = "test2", author = "author", rating=0, rating_count=2000)]
    srv = BookAnalyticsService()

    top_books = srv.top_rated(books)

    assert len(top_books) == 2
    assert top_books[0].title == "test"
    assert top_books[1].title == "test2"

def test_top_rated_negative():
    books = [1,2]
    svc = BookAnalyticsService()

    with pytest.raises(TypeError) as e:
        svc.top_rated(books)
        assert str(e.value) == 'Expected a Book list, got something else'

def test_value_scores_positive():
    books = [Book(book_id= "test", title = "test", author = "author", rating= 1, rating_count=1000, price_usd=50), 
             Book(book_id= "test2", title = "test",  author = "author", rating=.8, rating_count=2000, price_usd=60)]
    srv = BookAnalyticsService()

    book_values = srv.value_scores(books).keys()

    assert len(book_values) == 2

def test_value_scores_negative():
    books = [1,2]
    svc = BookAnalyticsService()

    with pytest.raises(TypeError) as e:
        svc.value_scores(books)
        assert str(e.value) == 'Expected a Book list, got something else'

def test_median_price_by_genre_positive():
    books = [Book(title= "test", author = "test", genre="History", price_usd=50), 
             Book(title= "test2",author = "test", genre="History", price_usd=51), 
             Book(title= "test3", author = "test", genre="Fantasy", price_usd=50)]
    srv = BookAnalyticsService()

    median_prices = srv.median_price_by_genre(books)

    assert len(median_prices) == 2
    assert median_prices["Fantasy"] == 50.0
    assert median_prices["History"] == 50.5

def test_median_price_by_genre_negative():
    books = [1,2]
    svc = BookAnalyticsService()

    with pytest.raises(TypeError) as e:
        svc.median_price_by_genre(books)
        assert str(e.value) == 'Expected a Book list, got something else'

def test_most_popular_genres_2026_positive():
    books = [Book(title= "test", author = "test", genre="History", price_usd=50, publication_year=2025), 
             Book(title= "test2",author = "test", genre="History", price_usd=51, publication_year=2025), 
             Book(title= "test3", author = "test", genre="Fantasy", price_usd=50, publication_year=2026)]
    srv = BookAnalyticsService()

    genres = srv.most_popular_genres_2026(books)

    assert len(genres) == 1
    assert genres["Fantasy"] == 1

def test_most_popular_genres_2026_negative():
    books = [1,2]
    svc = BookAnalyticsService()

    with pytest.raises(TypeError) as e:
        svc.most_popular_genres_2026(books)
        assert str(e.value) == 'Expected a Book list, got something else'  

def test_highest_rated_genres_positive():
    books = [Book(title= "test", author = "test", genre="History", rating=2, rating_count=50), 
             Book(title= "test2",author = "test", genre="History", rating=3, rating_count=100), 
             Book(title= "test3", author = "test", genre="Fantasy", rating=5, rating_count=40)]
    svc = BookAnalyticsService()

    genre_weight = svc.highest_rated_genres(books)

    assert len(genre_weight) == 2
    assert genre_weight["History"] == 2.8333333333333335
    assert genre_weight["Fantasy"] == 4.074074074074074
    
def test_highest_rated_genres_negative():
    books = [1,2]
    svc = BookAnalyticsService()

    with pytest.raises(TypeError) as e:
        svc.highest_rated_genres(books)
        assert str(e.value) == 'Expected a Book list, got something else'

def test_rating_vs_price_positive():
    books = [Book(title= "test", author = "test", price_usd=50, rating=2), 
             Book(title= "test2",author = "test", price_usd=51, rating=3), 
             Book(title= "test3", author = "test", price_usd=52, rating=5)]
    svc = BookAnalyticsService()

    rating_price = svc.rating_vs_price(books)

    assert len(rating_price) == 3
    assert rating_price[50] == 2


def test_rating_vs_price_negative():
    books = [1,2]
    svc = BookAnalyticsService()

    with pytest.raises(TypeError) as e:
        svc.rating_vs_price(books)
        assert str(e.value) == 'Expected a Book list, got something else'

def test_releases_by_year_positive():
    books = [Book(title= "test", author = "test", publication_year=1950), 
             Book(title= "test2",author = "test", publication_year=1950), 
             Book(title= "test3", author = "test", publication_year=1800)]
    svc = BookAnalyticsService()

    year_count = svc.releases_by_year(books)

    assert len(year_count) == 2
    assert year_count[1950] == 2
    assert year_count[1800] == 1

def test_releases_by_year_negative():
    books = [1,2]
    svc = BookAnalyticsService()

    with pytest.raises(TypeError) as e:
        svc.releases_by_year(books)
        assert str(e.value) == 'Expected a Book list, got something else'

def test_available_vs_unavailable_positive():
    books = [Book(title= "test", author = "test", available=True), 
             Book(title= "test2",author = "test", available=True), 
             Book(title= "test3", author = "test", available=False)]
    svc = BookAnalyticsService()

    available_unavailable = svc.available_vs_unavailable(books)

    assert len(available_unavailable) == 2
    assert available_unavailable["available"] == 2
    assert available_unavailable["unavailable"] == 1

def test_available_vs_unavailable_negative():
    books = [1,2]
    svc = BookAnalyticsService()

    with pytest.raises(TypeError) as e:
        svc.available_vs_unavailable(books)
        assert str(e.value) == 'Expected a Book list, got something else'