from library_structure import Library

def main():
    lib_settings = Library()

    while True:
        print("\nСистема управления библиотекой")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Введите ваш выбор: ")

        if choice == "1":
            title = input("Введите название: ")
            author = input("Введите автора: ")
            year = int(input("Введите год: "))
            lib_settings.add_book(title, author, year)
            print("Книга успешно добавлена.")

        elif choice == "2":
            book_id = input("Введите ID книги для удаления: ")
            try:
                lib_settings.remove_book(book_id)
                print("Книга успешно удалена.")
            except ValueError as e:
                print(e)

        elif choice == "3":
            title = input("Введите название (или нажмите Enter, чтобы пропустить): ") or None
            author = input("Введите автора (или нажмите Enter, чтобы пропустить): ") or None
            year = input("Введите год (или нажмите Enter, чтобы пропустить): ") or None
            if year:
                year = int(year)
            found_books = lib_settings.find_books(title, author, year)
            if found_books:
                for book in found_books:
                    print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
            else:
                print("Книги не найдены.")

        elif choice == "4":
            lib_settings.display_books()

        elif choice == "5":
            book_id = input("Введите ID книги для изменения статуса: ")
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            try:
                lib_settings.change_book_status(book_id, new_status)
                print("Статус книги успешно изменен.")
            except ValueError as e:
                print(e)

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
