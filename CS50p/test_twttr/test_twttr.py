from twttr import shorten


def test_shorten():
    assert shorten("abcde") == "bcd"
    assert shorten("Abcde") == "bcd"
    assert shorten("abcde123") == "bcd123"
    assert shorten("ABCDE") == "BCD"
    assert shorten("abcde!!!") == "bcd!!!"
