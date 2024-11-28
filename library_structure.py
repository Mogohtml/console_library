import json
import os
import uuid

class Book:
    def __init__(self, title, author, year, book_id=None, status="в наличии"):
        self.title = title
        self.author = author
        self.year = year
        self.id = book_id if book_id else self.generate_id()
        self.status = status

    def generate_id(self):
        return uuid.uuid4().hex.upper()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(book_dict):
        return Book(
            book_id=book_dict["id"],
            title=book_dict["title"],
            author=book_dict["author"],
            year=book_dict["year"],
            status=book_dict["status"]
        )

class Library:
    def __init__(self, file_path="books.json"):
        self.file_path = file_path
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                books_data = json.load(file)
                return [Book.from_dict(book) for book in books_data]
        return []

    def save_books(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4, ensure_ascii=False)

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save_books()

    def remove_book(self, book_id):
        self.books = [book for book in self.books if book.id != book_id]
        self.save_books()

    def find_books(self, title=None, author=None, year=None):
        return [book for book in self.books if (
            (title is None or book.title == title) and
            (author is None or book.author == author) and
            (year is None or book.year == year)
        )]

    def display_books(self):
        for book in self.books:
            print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")

    def change_book_status(self, book_id, new_status):
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books()
                return
        raise ValueError("Книга не найдена")
