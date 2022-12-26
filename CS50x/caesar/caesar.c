#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

string shift_text(string text);
int cipher;

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (isdigit((argv[1])[i]))
            {
                //printf("%c is a digit\n", (argv[1])[i]);
            }
            else
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
        cipher = atoi(argv[1]);
        //printf("test %c\n", (argv[1])[1]);

        string text = get_string("plaintext:  ");
        cipher = cipher % 26;
        string new_text = shift_text(text);
        printf("ciphertext: %s\n", new_text);
    }
}

string shift_text(string text)
{
    for (int i = 0, n = strlen(text), convert = 0; i < n; i++)
    {
        if (isalpha(text[i]))
        {
            if (islower(text[i]))
            {
                text [i] = toupper(text[i]);
                convert++;
            }
            text[i] += cipher;
            if (text[i] > 90)
            {
                text[i] -= 26;
            }
            if (convert != 0)
            {
                text [i] = tolower(text[i]);
                convert = 0;
            }
        }
    }
    return text;
}