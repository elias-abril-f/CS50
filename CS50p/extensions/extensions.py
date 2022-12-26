def main():
    extensions = [".gif", ".bmp", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]
    images = [".gif", ".jpg", ".jpeg", ".png", ".bmp"]
    other = [".zip", ".pdf", ".txt"]
    i = input("File name: ").lower().strip()
    r = check(i, extensions, images, other)
    print(r)


def check(i, extensions, images, other):
    temp = ""
    for extension in extensions:
        if extension in i:
            temp = extension.replace(".", "")
            if extension in images:
                if extension == ".jpg" or extension == ".jpeg":
                    temp = "image/jpeg"
                    break
                else:
                    temp = (f"image/{temp}")
                    break
            if extension in other:
                if extension == ".txt":
                    temp = ("text/plain")
                    break
                elif extension == ".pdf":
                    temp = ("application/pdf")
                    break
                elif extension == ".zip":
                    temp = ("application/zip")
                    break
        else:
            temp = "application/octet-stream"

    return temp


main()