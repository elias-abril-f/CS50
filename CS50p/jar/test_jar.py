from jar import Jar
import pytest


def test_create():
    jar = Jar()
    assert jar.capacity == 12
    jar1 = Jar(1)
    assert jar1.capacity == 1


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1


def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    assert jar.size == 1


def test_print():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(2)
    assert str(jar) == "🍪🍪"


def test_errors():
    with pytest.raises(ValueError):
        jar = Jar(-1)

    with pytest.raises(ValueError):
        jar = Jar()
        jar.withdraw(1)

    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(13)

    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(-1)

    with pytest.raises(ValueError):
        jar = Jar()
        jar.withdraw(-1)
