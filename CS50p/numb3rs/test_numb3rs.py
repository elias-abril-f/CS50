from numb3rs import validate


def testValidate():
    assert validate("1.1.1.1") == True
    assert validate("1.256.256.256") == False
    assert validate("1.1.2000.1") == False
    assert validate("foo") == False


if __name__ == "__test_validate__":
    testValidate()
