import pytest

from src.widget import get_date, mask_account_card


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2014-03-11T02:26:18.671407") == "11.03.2014"
    with pytest.raises(ValueError):
        get_date("")


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
