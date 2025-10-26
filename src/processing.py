def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция которая возвращает новый список словарей в соответствии с аргументом state"""
    new_list_dict = []

    for sta in list_dict:
        if sta.get("state") == state:
            new_list_dict.append(sta)

    return new_list_dict


def sort_by_date(list_dict: list, date: bool = True) -> list:
    """Функция сортировки списка словарей по дате (по умолчанию - убывание)"""
    sorted_list_dict = sorted(list_dict, key=lambda x: x.get("date"), reverse=date)

    return sorted_list_dict
