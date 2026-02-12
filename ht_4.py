from typing import Dict, Optional, Tuple

BOOKS = [
    {'genre': 'поэзия', 'number': '978-5-1000-1234-7', 'title': 'Евгений Онегин', 'author': 'Александр Пушкин'},
    {'genre': 'фэнтези', 'number': '88006', 'title': 'Властелин колец', 'author': 'Джон Р. Р. Толкин'},
    {'genre': 'детектив', 'number': 'D-1122', 'title': 'Безмолвный свидетель', 'author': 'Агата Кристи'}
]

DIRECTORIES = {
    '1': ['978-5-1000-1234-7', '88006'],
    '2': ['D-1122'],
    '3': []
}

books_by_id: Dict[str, dict] = {b['number']: b for b in BOOKS}
books_by_title: Dict[str, dict] = {b['title']: b for b in BOOKS}
id_to_shelf: Dict[str, str] = {
    book_id: shelf_id 
    for shelf_id, book_ids in DIRECTORIES.items() 
    for book_id in book_ids
}
shelves = DIRECTORIES

def get_book_info(book_id: str) -> Optional[Tuple[str, str]]:
    book = books_by_id.get(book_id)
    return (book['title'], book['author']) if book else None

def add_shelf(shelf_id: str) -> None:
    if shelf_id in shelves:
        print(f"Такая полка уже существует. Полки: {list(shelves.keys())}")
        return
    shelves[shelf_id] = []
    print(f"Полка добавлена. Полки: {list(shelves.keys())}")

def del_shelf(shelf_id: str) -> None:
    if shelf_id not in shelves:
        print(f"Такой полки не существует. Полки: {list(shelves.keys())}")
        return
    if shelves[shelf_id]:
        print("На полке есть книги, удалите их перед удалением полки.")
        return
    del shelves[shelf_id]
    print(f"Полка удалена. Полки: {list(shelves.keys())}")

def show_all() -> None:
    for b_id, book in books_by_id.items():
        shelf = id_to_shelf.get(b_id, "Не назначена")
        print(f"№: {b_id}, жанр: {book['genre']}, название: {book['title']}, "
              f"автор: {book['author']}, полка: {shelf}")

def main():
    while True:
        cmd = input("\nВведите команду (book_info, shelf, all, add_shelf, del_shelf, q):\n").strip()
        match cmd:
            case "book_info":
                b_id = input("Введите номер книги:\n")
                info = get_book_info(b_id)
                if info:
                    print(f"Название книги: {info[0]}\nАвтор: {info[1]}")
                else:
                    print("Книга не найдена в базе")
            case "shelf":
                title = input("Введите название книги:\n")
                book = books_by_title.get(title)
                shelf = id_to_shelf.get(book['number']) if book else None
                if shelf:
                    print(f"Книга хранится на полке: {shelf}")
                else:
                    print("Книга не найдена в базе")
            case "all":
                show_all()
            case "add_shelf":
                add_shelf(input("Введите номер полки:\n"))
            case "del_shelf":
                del_shelf(input("Введите номер полки:\n"))
            case "q":
                break
            case _:
                print("Неизвестная команда")

if __name__ == "__main__":
    main()
