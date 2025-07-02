"""Функция реализует маскировки счета"""

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def get_mask_account(personal_account: int) -> str:
    personal_account_str = str(personal_account)
    if len(personal_account_str) == 20:
        nomber_card_number = f"**{personal_account_str[-4:]}"
        logging.info(nomber_card_number)
        return nomber_card_number
    else:
        logging.error(f"Не правильно gg ")
        return "Не правильно"


"""Функция реализует маскировки номера"""


def get_mask_card_number(personal_card: int) -> str:
    personal_card_str = str(personal_card)
    if len(personal_card_str) == 16:
        nomber_card_numbe = f"{personal_card_str[:4]} {personal_card_str[4:6]} ** *** {personal_card_str[12:]}"
        logging.info(nomber_card_numbe)
        return nomber_card_numbe
    else:
        logging.error(f"Не правильно")
        return f"Не правильно"
