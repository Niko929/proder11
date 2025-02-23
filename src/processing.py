from typing import List, Dict

"""Функция фильтрует данные ключ которых совпадаетс аргументом state"""


def filter_by_state(rey_fultr: List[Dict[str,int]], state="EXECUTED") -> list[dict[str,int]]:
    # ter = []
    #  for req in rey_fultr:
    # if req["state"] == state:
    # ter.append(req)
    return [req for req in rey_fultr if req.get("state") == state]


""" Функция сортирует данные по дате, от больше к меньшему"""


def sort_by_date(sort_dat: list[dict], reverse: bool = True) -> list[dict]:
    hg = sorted(sort_dat, key=lambda x: x["date"], reverse=reverse)
    return hg
