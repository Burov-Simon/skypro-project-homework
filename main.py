from src.generators import filter_by_currency
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.transaction_reader import (path_file_csv, path_file_excel,
                                    trans_reader_csv, trans_reader_excel)
from src.utils import get_file_operations
from src.widget import get_date, mask_account_card


def main():
    while True:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        user_choice = input().strip()

        if user_choice == "1":
            file_json_path = "data/operations.json"
            transactions = get_file_operations(file_json_path)
            print("Был выбран JSON")
            break
        elif user_choice == "2":
            file_csv_path = "data/transactions.csv"
            transactions = trans_reader_csv(file_csv_path)
            print("Был выбран CSV")
            break
        elif user_choice == "3":
            file_excel_path = "data/transactions_excel.xlsx"
            transactions = trans_reader_excel(file_excel_path)
            print("Был выбран XLSX")
            break
        else:
            print(f"Данный выбор {user_choice} не доступен")
            continue

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = ["EXECUTED", "CANCELED", "PENDING"]
        user_status_choice = input().upper().strip()
        if user_status_choice in status:
            status_filter = user_status_choice
            print(f"Был выбран статус: {status_filter}")
            ft = filter_by_state(transactions, status_filter)
            break
        else:
            print(f"Статус операции {user_status_choice} недоступен")
            continue

    while True:
        sort_by_date_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
        if sort_by_date_choice == "да":
            order_choice = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
            if order_choice == "по возрастанию":
                order_filter = False
                ft = sort_by_date(ft, order_filter)
                break
            else:
                break
        else:
            break

    while True:
        currency_choice = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
        if currency_choice in ("да", "нет"):
            if currency_choice.lower() == "да" and user_choice in ["2", "3"]:
                ft = [t for t in ft if t.get("currency_code") == "RUB"]
                break
            elif currency_choice.lower() == "да" and user_choice == "1":
                ft = list(filter_by_currency(ft, "RUB"))
                break
            if currency_choice.lower() == "нет":
                break

    while True:
        word_for_filter = (
            input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").strip().lower()
        )
        if word_for_filter in ["да", "нет"]:
            if word_for_filter == "да":
                filter_word = input("Введите слово:\n")
                ft = process_bank_search(ft, filter_word)
                break
            else:
                break
        else:
            continue

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(ft)}")
    print(ft)


some_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
    print(filter_by_state(some_dict))
    print(sort_by_date(some_dict))
    print(trans_reader_csv(path_file_csv))
    print(trans_reader_excel(path_file_excel))
    print(main())
