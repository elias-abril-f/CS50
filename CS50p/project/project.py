import ffmpeg
import re
import sys


from pytube import YouTube


def main():
    arg = "nottest"
    url = f"https://youtu.be/{userIn({arg})}"
    title, vidFormat, audFormat = youtube(url)
    combine(title, vidFormat, audFormat)


def combine(title, vidFormat, audFormat):
    if title == "test":
        return "Cool beans"
    input_video = ffmpeg.input(f"test/video/{title}.{vidFormat}")
    input_audio = ffmpeg.input(f"test/audio/{title}.{audFormat}")
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(f"{title}.mp4").run()


def userIn(test):
    if test == "test":
        return "oh yeah"
    while True:
        try:
            i = input("Link: ")
            url = re.search(r"^(?:https?://)?(?:www\.)youtube\.com/watch\?v=(\w{11})", i, re.IGNORECASE)[1]
            if not url:
                continue
            return url
        except:
            continue


def youtube(url):
    yt = YouTube(url)
    video = f"{yt.streams.filter(only_video=True)}".split(", ")
    audio = f"{yt.streams.filter(only_audio=True)}".split(", ")
    vid, vidFormat = extract_max(video)
    print(vid)
    aud, audFormat = extract_max(audio)
    print(aud)

    vidStream = yt.streams.get_by_itag(vid)
    vidStream.download("test/video", filename=f"{yt.title}.{vidFormat}")
    audStream = yt.streams.get_by_itag(aud)
    audStream.download("test/audio", filename=f"{yt.title}.{audFormat}")
    return yt.title, vidFormat, audFormat


def extract_max(inp):
    streams = {}
    for i in inp:
        print(i)
        if not "kbps" in i:
            temp = re.search(r'^\[?<Stream: itag="(.{3})" mime_type="video/(webm|mp4)" res="(360|480|720|1080|1440|2160)p" fps=".?..fps" vcodec=".+" progressive="False" type="video">\]?$', i, re.IGNORECASE)
        else:
            temp = re.search(r'^\[?<Stream: itag="(.{3})" mime_type="audio/(mp4|webm)" abr="(128|160)kbps" acodec=".+" progressive="False" type="audio">\]?$', i, re.IGNORECASE)
        try:
            if temp[3]:
                streams[temp[1]] = temp[3]
                format = temp[2]
        except:
            continue
    try:
        print(streams)
        return max(streams), format
    except:
        sys.exit("Not enough quality")


if __name__ == "__main__":
    main()
