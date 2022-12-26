
from cs50 import get_string

wordCount = 0
letterCount = 0
sentencesCount = 0


def main():
    text = get_string("Give it to me baby: ")

    letterCount = countLetters(text)
    # print(f"Number of Letters: {letterCount}")

    wordCount = countWords(text)
    # print(f"Number of Words: {wordCount}")

    sentencesCount = countSentences(text)
    # print(f"Number of Sentences: {sentencesCount}")

    level = round(formula(letterCount, wordCount, sentencesCount))
    if level < 1:
        print("Before Grade 1")
    elif level > 16:
        print("Grade 16+")
    else:
        print(f"Grade {level}")


def countLetters(text):
    count = 0
    length = len(text)
    for i in range(0, length, 1):
        tmp = text[i]
        if tmp.isalpha():
            count += 1
    return count


def countWords(text):
    tmp = 0
    count = 1
    length = len(text)
    for i in range(0, length, 1):
        tmp = text[i]
        if tmp.isspace():
            count += 1
    return count


def countSentences(text):
    tmp = 0
    count = 0
    length = len(text)
    for i in range(0, length, 1):
        tmp = text[i]
        if (tmp == "." or tmp == "?" or tmp == "!"):
            count += 1
    return count

# Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per 100 words in the text,
# and S is the average number of sentences per 100 words in the text
# L = (letters / (float) words) * 100; S = (sentences / (float) words) * 100;


def formula(letters, words, sentences):
    L = (letters / words) * 100
    S = (sentences / words) * 100

    lvl = 0.0588 * L - 0.296 * S - 15.8
    return lvl


if __name__ == "__main__":
    main()
