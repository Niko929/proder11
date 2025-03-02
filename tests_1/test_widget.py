import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("date_1 , date_2",[
    ("2024-03-11T02:26:18.671407" , "11.03.2024"),
    ("2025-03-11T02:26:18.671407" , "11.03.2025"),
])
def test_get_date(date_1 , date_2):
    assert get_date(date_1) == date_2


@pytest.mark.parametrize(
    "parat1 , parat2",
    [
        ("Счет 15487459861254495898", "Счет **5898"),
        ("Visa Gold 1548745985216125", "VisaGold 1548 74 ** *** 6125"),
        ("Visa 1548745985216255", "Не правильно введены значения"),
        ("", "Не правильно введены значения"),
    ],
)
def test_mask_account_card(parat1, parat2):
    assert mask_account_card(parat1) == parat2
