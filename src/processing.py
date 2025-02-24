from typing import Any, Dict, List


def filter_by_state(rey_fultr: List[Dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрует данные ключ которых совпадают по значению с параметром state"""
    # ter = []
    #  for req in rey_fultr:
    # if req["state"] == state:
    # ter.append(req)
    return [req for req in rey_fultr if req.get("state") == state]


def sort_by_date(sort_dat: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортирует данные по дате, от большего к меньшему"""
    hg = sorted(sort_dat, key=lambda x: x["date"], reverse=reverse)
    return hg
