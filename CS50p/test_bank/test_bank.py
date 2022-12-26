from bank import value


def test_value ():
    assert value("hello") == 0
    assert value("Hilkjh") == 20
    assert value("foolkjhalsdf") == 100
