from um import count


def test_count():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("um, ") == 1
    assert count("um?") == 1
    assert count("umma") == 0
    assert count("yum") == 0
    assert count("Um, thanks, um...") == 2