def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция которая возвращает новый список словарей в соответствии с аргументом state"""
    new_list_dict = []

    for sta in list_dict:
        if sta.get("state") == state:
            new_list_dict.append(sta)

    return new_list_dict
