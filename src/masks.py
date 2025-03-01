"""Функция реализует маскировки счета"""


def get_mask_account(personal_account: int) ->str:
    personal_account_str = str(personal_account)
    if len(personal_account_str) == 20:
        nomber_card_number = f"**{personal_account_str[-4:]}"
        return nomber_card_number

    else:
        return "Не правильно"


"""Функция реализует маскировки номера"""


def get_mask_card_number(personal_card: int) ->str:
    personal_card_str = str(personal_card)
    if len(personal_card_str) == 16:
        nomber_card_numbe = f"{personal_card_str[:4]} {personal_card_str[4:6]} ** *** {personal_card_str[12:]}"
        return nomber_card_numbe

    else:
        return "Не правильно"
