# YOUTUBE MAX QUALITY DOWNLOADER
#### Video Demo:  https://www.youtube.com/watch?v=VhT0jCpCawE
#### Description:
This is a youtube downloader that leverages the power of pytube library and ffmpeg to archieve
maximum quality in downloads from YouTube.

All you need to do is run the program and at first it will ask for a link. Paste it.
The python script will check the link given and compare it to a regular expression to check if
it is a valid YouTube link. If it is, it will extract the address to the wanted video and
eliminate the rest. After doing that, it will add it to a
prefixed generic and shorter YouTube URL
(https://youtu.be/).

The next step is querying YouTube for said video. If everything goes alright, the next function
in the python script will request all the non progresive streams (not the ones where the video
and the audio is in one file, as this way we are limited to 720p), first video and and then audio.
The information received is converted to a string, stripped of any whitespace and unnecessary
characters and then parsed onto a list. This list is then passed to another function that will
determine the hightest quality video and audio streams.

Next step in out journey is finding the best of the best. This function receives the raw
information and compares it to another regular expresssion. In this case it extracts the format
and the resolution if it is a video file or the format and the rate if it is an audio file,
adding the data to a dictionary, where the key is the stream id and the value the quality. After
all the streams are analysed, it runs a max function to find the highest quality and then it
returns it to the previous function, where the selected stream is downloaded. Audio and video
files are downloaded in different folders for easy archiving and to facilitate the possibility
of deleting one or the other depending on our case use (a musical video might be useless
without audio, so we might want to keep just the audio file, but a decorative video for a smart
photo display might be ok to keep without audio).

Last using the ffmpeg-python library we combine both files into one high quality video. The speed
of this process will depend on the quality of our computer, but it is worth the wait, as at the
end we will have out desired video in the highest quality available!! 