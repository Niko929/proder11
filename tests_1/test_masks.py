import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("1548745985216125", "1548 74 ** *** 6125"),
        ("1545248788843157", "1545 24 ** *** 3157"),
        ("7485125485656556", "7485 12 ** *** 6556"),
        ("154874598521645888", "Не правильно"),
        ("", "Не правильно"),
    ],
)
def test_mask_card_number(string, expected_result):
    assert get_mask_card_number(string) == expected_result


@pytest.mark.parametrize(
    "string1, expected_result1",
    [
        ("15487459852164225828", "**5828"),
        ("15452487888431578545", "**8545"),
        ("74851254856565568546", "**8546"),
        ("154874598521645888", "Не правильно"),
        ("", "Не правильно"),
    ],
)
def test_get_mask_account(string1, expected_result1):
    assert get_mask_account(string1) == expected_result1
