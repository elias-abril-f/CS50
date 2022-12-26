from seasons import validate
from datetime import date
import pytest

def test_validate_correct():
    assert validate("2021-10-10") == "Five hundred twenty-five thousand, six hundred"
    assert validate("2020-10-10") == "One million, fifty-one thousand, two hundred"
