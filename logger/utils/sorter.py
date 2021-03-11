def sorter_list_by_key(data: list, dict_key: str) -> list:
    """
    Сортировка словарей в списке по выбранной строке-ключу.
    Строка должна состоять из цифр или форматом даты.
    """
    for i in range(1, len(data)):
        cursor = data[i]
        pos = i - 1

        while pos >= 0 and data[pos][dict_key] > cursor[dict_key]:

            data[pos + 1] = data[pos]
            pos = pos - 1

        data[pos + 1] = cursor

    return data

