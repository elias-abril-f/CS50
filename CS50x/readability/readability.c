#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int letters = 0;
int words = 0;
int sentences = 0;

int main(void)
{
    string text = get_string("Your text: ");

    letters = count_letters(text);
    //printf("Total letters: %i\n", letters);

    words = count_words(text);
    //printf("Total word: %i\n", words);

    sentences = count_sentences(text);
    //printf("Total sentences: %i\n", sentences);

    float L = (letters / (float) words) * 100;
    float S = (sentences / (float) words) * 100;

    float subindex = 0.0588 * L - 0.296 * S - 15.8;
    int index = round(subindex);

    //printf("Index is : %i\n", index);

    if (index > 16)
    {
        printf("Grade 16+\n");
    }

    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }

    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string text)
{
    int total = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            total++;
            //printf("Total letters: %i\n", letter);
        }
    }
    return (total);
}

int count_words(string text)
{
    int total = 1;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isspace(text[i]))
        {
            total++;
        }
    }
    return (total);
}

int count_sentences(string text)
{
    int total = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (((text[i]) == 46) || ((text[i]) == 33) || ((text[i]) == 63))
        {
            total++;
        }
    }
    return (total);
}

