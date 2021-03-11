import datetime


def dict_extractor(data: list, *args: str) -> list:
    """Создает новый список словарей по указанным ключам."""
    ext_data = [{key: value for key, value in log.items()
                    if key in args}
                        for log in data]

    return ext_data


def dict_val_conv(data: list, *args: str) -> list:
    """Преобразует строки значений списка словарей в числа."""
    conv_data = [{key: (int(value) if key in args else value)
                    for key, value in log.items()}
                        for log in data]

    return conv_data


def dict_date_conv(data: list, *args: str) -> list:
    """Преобразует дату в списке словарей."""
    conv_date = [{key: (datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
                            if key in args else value)
                    for key, value in log.items()}
                        for log in data]

    return conv_date

