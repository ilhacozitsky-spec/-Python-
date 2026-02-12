from typing import Optional, List, Dict

BOOKS = [
    {
        "genre": "поэзия",
        "number": "978-5-1000-1234-7",
        "title": "Евгений Онегин",
        "author": "Александр Пушкин",
    },
    {
        "genre": "фэнтези",
        "number": "88006",
        "title": "Властелин колец",
        "author": "Джон Р. Р. Толкин",
    },
    {
        "genre": "детектив",
        "number": "D-1122",
        "title": "Безмолвный свидетель",
        "author": "Агата Кристи",
    },
]

DIRECTORIES = {"1": ["978-5-1000-1234-7", "88006"], "2": ["D-1122"], "3": []}


class Library:
    def __init__(self, books: List[dict], shelves: Dict[str, List[str]]):
        self.books = books.copy()
        self.shelves = shelves.copy()

    def _find_by_id(self, book_id: str) -> Optional[dict]:
        for book in self.books:
            if book["number"] == book_id:
                return book
        return None

    def _find_by_title(self, title: str) -> Optional[dict]:
        for book in self.books:
            if book["title"] == title:
                return book
        return None

    def _get_shelf_for_book(self, book_id: str) -> Optional[str]:
        for shelf_id, book_ids in self.shelves.items():
            if book_id in book_ids:
                return shelf_id
        return None

    def book_info(self, book_id: str) -> None:
        book = self._find_by_id(book_id)
        if book:
            print(f"Название книги: {book['title']}\nАвтор: {book['author']}")
        else:
            print("Книга не найдена в базе")

    def shelf_info(self, title: str) -> None:
        book = self._find_by_title(title)
        if book:
            shelf = self._get_shelf_for_book(book["number"])
            if shelf:
                print(f"Книга хранится на полке: {shelf}")
                return
        print("Книга не найдена в базе")

    def show_all(self) -> None:
        for book in self.books:
            shelf = self._get_shelf_for_book(book["number"]) or ""
            print(
                f"№: {book['number']}, жанр: {book['genre']}, "
                f"название: {book['title']}, автор: {book['author']}, "
                f"полка хранения: {shelf}"
            )

    def add_shelf(self, shelf_id: str) -> None:
        if shelf_id in self.shelves:
            shelves = ", ".join(self.shelves.keys())
            print(f"Такая полка уже существует. Текущий перечень полок: {shelves}.")
            return
        self.shelves.setdefault(shelf_id, [])
        shelves = ", ".join(self.shelves.keys())
        print(f"Полка добавлена. Текущий перечень полок: {shelves}.")

    def del_shelf(self, shelf_id: str) -> None:
        if shelf_id not in self.shelves:
            shelves = ", ".join(self.shelves.keys())
            print(f"Такой полки не существует. Текущий перечень полок: {shelves}.")
            return
        if self.shelves[shelf_id]:
            shelves = ", ".join(self.shelves.keys())
            print(
                f"На полке есть книги, удалите их перед удалением полки. "
                f"Текущий перечень полок: {shelves}."
            )
            return
        del self.shelves[shelf_id]
        shelves = ", ".join(self.shelves.keys())
        print(f"Полка удалена. Текущий перечень полок: {shelves}.")

    def add_book(
        self, book_id: str, genre: str, title: str, author: str, shelf_id: str
    ) -> None:
        if self._find_by_id(book_id):
            print("Книга с таким номером уже существует.")
            self.show_all()
            return

        if shelf_id not in self.shelves:
            print("Такой полки не существует. Добавьте полку командой add_shelf.")
            self.show_all()
            return

        self.books.append(
            {"genre": genre, "number": book_id, "title": title, "author": author}
        )
        self.shelves[shelf_id].append(book_id)

        print("Книга добавлена.")
        self.show_all()

    def del_book(self, book_id: str) -> None:
        book = self._find_by_id(book_id)
        if not book:
            print("Книга не найдена в базе.")
            self.show_all()
            return

        self.books.remove(book)

        shelf = self._get_shelf_for_book(book_id)
        if shelf:
            self.shelves[shelf].remove(book_id)

        print("Книга удалена.")
        self.show_all()

    def move_book(self, book_id: str, new_shelf_id: str) -> None:
        if not self._find_by_id(book_id):
            print("Книга не найдена в базе.")
            self.show_all()
            return

        if new_shelf_id not in self.shelves:
            shelves = ", ".join(self.shelves.keys())
            print(f"Такой полки не существует. Текущий перечень полок: {shelves}.")
            return

        old_shelf = self._get_shelf_for_book(book_id)
        if old_shelf:
            self.shelves[old_shelf].remove(book_id)

        self.shelves[new_shelf_id].append(book_id)

        print("Книга перемещена.")
        self.show_all()


def main():
    library = Library(BOOKS, DIRECTORIES)

    while True:
        cmd = input(
            "\nВведите команду (book_info, shelf, all, add_shelf, "
            "del_shelf, add_book, del_book, move, q):\n"
        ).strip()

        match cmd:
            case "book_info":
                book_id = input("Введите номер книги:\n")
                library.book_info(book_id)

            case "shelf":
                title = input("Введите название книги:\n")
                library.shelf_info(title)

            case "all":
                library.show_all()

            case "add_shelf":
                shelf_id = input("Введите номер полки:\n")
                library.add_shelf(shelf_id)

            case "del_shelf":
                shelf_id = input("Введите номер полки:\n")
                library.del_shelf(shelf_id)

            case "add_book":
                book_id = input("Введите номер книги:\n")
                genre = input("Введите жанр книги:\n")
                title = input("Введите название книги:\n")
                author = input("Введите автора книги:\n")
                shelf_id = input("Введите полку для хранения:\n")
                library.add_book(book_id, genre, title, author, shelf_id)

            case "del_book":
                book_id = input("Введите номер книги:\n")
                library.del_book(book_id)

            case "move":
                book_id = input("Введите номер книги:\n")
                shelf_id = input("Введите номер полки:\n")
                library.move_book(book_id, shelf_id)

            case "q":
                break

            case _:
                print("Неизвестная команда")


if __name__ == "__main__":
    main()
