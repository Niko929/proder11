import datetime
from typing import Any

from src.masks import get_mask_account, get_mask_card_number

title = "Visa Platinum", "Maestro", "MasterCard", "Visa Classic", "Visa Gold"


def mask_account_card(name_card: Any) -> Any:
    text_card = ""
    nomer_card = ""
    if name_card.startswith(title):
        for ter in name_card:
            if ter.isalpha():
                text_card += ter
            if ter.isdigit():
                nomer_card += ter
        return f"{text_card} {get_mask_card_number(int(nomer_card))}"
    elif name_card.startswith("Счет"):
        for ter in name_card:
            if ter.isalpha():
                text_card += ter
            if ter.isdigit():
                nomer_card += ter
        return f"{text_card} {get_mask_account(int(nomer_card))}"
    else:
        return "Не правильно введены значения"


def get_date(pippppp: Any) -> str:
    date_format = datetime.datetime.strptime(pippppp, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date
