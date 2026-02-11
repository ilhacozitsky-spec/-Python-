# Задание 1

from datetime import datetime, timedelta

# Глобальная константа для стандартного формата даты
DATE_FORMAT = "%Y-%m-%d"


def task_1() -> None:
    """
    Печатные газеты использовали свой формат дат для каждого выпуска.
    Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime.
    """
    newspapers = [
        ("The Moscow Times", "Wednesday, October 2, 2002", "%A, %B %d, %Y"),
        ("The Guardian", "Friday, 11.10.13", "%A, %d.%m.%y"),
        ("Daily News", "Thursday, 18 August 1977", "%A, %d %B %Y"),
    ]

    for name, date_str, fmt in newspapers:
        dt = datetime.strptime(date_str, fmt)
        print(f"{name}: {dt}")

# Задание 2

def validate_dates(stream: list[str]) -> list[bool]:
    """
    Проверяет даты на корректность в формате YYYY-MM-DD.
    Возвращает True — дата корректна или False — некорректная.
    """
    results: list[bool] = []
    for date_str in stream:
        try:
            datetime.strptime(date_str, DATE_FORMAT)
            results.append(True)
        except ValueError:
            results.append(False)
    return results

# Задание 3

def date_range(start_date: str, end_date: str) -> list[str]:
    """
    Возвращает список дат за период от start_date до end_date в формате YYYY-MM-DD.
    В случае неверного формата или при start_date > end_date возвращается пустой список.
    """
    try:
        start_dt = datetime.strptime(start_date, DATE_FORMAT)
        end_dt = datetime.strptime(end_date, DATE_FORMAT)
    except ValueError:
        return []

    if start_dt > end_dt:
        return []

    res: list[str] = []
    current_dt = start_dt
    while current_dt <= end_dt:
        res.append(current_dt.strftime(DATE_FORMAT))
        current_dt += timedelta(days=1)

    return res

# Проверка 

if __name__ == "__main__":
    print("--- Задание 1 ---")
    task_1()

    print("\n--- Задание 2 ---")
    stream = ["2018-04-02", "2018-02-29", "2018-19-02"]
    validity = validate_dates(stream)
    for s, v in zip(stream, validity):
        status = "Корректна" if v else "Некорректна"
        print(f"Дата {s}: {status}")

    print("\n--- Задание 3 ---")
    test_ranges = [
        ("2022-01-01", "2022-01-06", "Нормальный диапазон"),
        ("2022-01-01", "2022-13-01", "Ошибка формата"),
        ("2022-01-02", "2022-01-01", "Начало позже конца"),
    ]

    for start, end, label in test_ranges:
        result = date_range(start, end)
        print(f"{label} [{start} - {end}]: {result}")
