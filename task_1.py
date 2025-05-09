import pytest
from books_collector import BooksCollector

# Проверка добавления новой книги
@pytest.mark.parametrize('book_name', ['Властелин колец', 'Гарри Поттер', ''])
def test_add_new_book(book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    if book_name and len(book_name) <= 40:
        assert book_name in collector.get_books_genre()
        assert collector.get_book_genre(book_name) == ''
    else:
        assert book_name not in collector.get_books_genre()

# Проверка ограничения в 40 символов
def test_add_new_book_with_long_name():
    collector = BooksCollector()
    long_name = 'К' * 41
    collector.add_new_book(long_name)
    assert long_name not in collector.get_books_genre()

# Проверка установки жанра
def test_set_book_genre():
    collector = BooksCollector()
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

# Проверка, что нельзя установить несуществующий жанр
def test_set_book_genre_invalid_genre():
    collector = BooksCollector()
    collector.add_new_book('Гарри Поттер')
    collector.set_book_genre('Гарри Поттер', 'Поэзия')
    assert collector.get_book_genre('Гарри Поттер') == ''

# Проверка получения книг с конкретным жанром
def test_get_books_with_specific_genre():
    collector = BooksCollector()
    collector.add_new_book('Книга 1')
    collector.add_new_book('Книга 2')
    collector.set_book_genre('Книга 1', 'Фантастика')
    collector.set_book_genre('Книга 2', 'Комедии')
    result = collector.get_books_with_specific_genre('Фантастика')
    assert result == ['Книга 1']

# Проверка фильтрации книг без возрастного рейтинга
def test_get_books_for_children():
    collector = BooksCollector()
    collector.add_new_book('Детская')
    collector.add_new_book('Ужастик')
    collector.set_book_genre('Детская', 'Мультфильмы')
    collector.set_book_genre('Ужастик', 'Ужасы')
    result = collector.get_books_for_children()
    assert result == ['Детская']

# Проверка добавления книги в избранное
def test_add_book_in_favorites():
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.add_book_in_favorites('Книга')
    assert collector.get_list_of_favorites_books() == ['Книга']

# Проверка удаления книги из избранного
def test_delete_book_from_favorites():
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.add_book_in_favorites('Книга')
    collector.delete_book_from_favorites('Книга')
    assert collector.get_list_of_favorites_books() == []

# Проверка невозможности добавления книги дважды в избранное
def test_add_book_in_favorites_twice():
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.add_book_in_favorites('Книга')
    collector.add_book_in_favorites('Книга')
    assert collector.get_list_of_favorites_books() == ['Книга']
