from project import combine, userIn, youtube, extract_max
import pytube

def test_combine():
    assert combine("test", "webm", "mp4") == "Cool beans"


def test_userIn():
    assert userIn("test") == "oh yeah"


def test_youtube():
    assert youtube("https://youtu.be/5AhZh4A7NLM") == ("i want to die", "mp4", "webm")


def test_extract_max():
    yt = pytube.YouTube("https://youtu.be/5AhZh4A7NLM")
    video = f"{yt.streams.filter(only_video=True)}".split(", ")
    assert extract_max(video) == ('399', 'mp4')