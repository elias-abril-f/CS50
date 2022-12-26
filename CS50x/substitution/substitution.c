#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int checkKey(int argc, string key);
string subText(string text, string code, int length);

string plaintext;
string ciphertext;

int main(int argc, string argv[])
{
    if (checkKey(argc, argv[1]) == 0)
    {
        plaintext = get_string("plaintext:  ");
        int length = strlen(plaintext);
        ciphertext = subText(plaintext, argv[1], length);
        printf("ciphertext: %s\n", ciphertext);
    }

    else
    {
        return 1;
    }
}

int checkKey(int argc, string key)
{
    if (argc == 2)
    {
        if (strlen(key) == 26)
        {
            for (int i = 0, c[26], index = 0; i < 26; i++)
            {
                if (isalpha(key[i]))
                {
                    key[i] = toupper(key[i]);
                    // printf("%c  ", key[i]);
                    index = key[i] - 65;
                    // printf("%i  ", index);
                    c[index]++;
                    // printf("%i\n", c[index]);
                    if (c[index] > 1)
                    {
                        printf("Letters cannot be repeated\n");
                        return 4;
                    }
                }
                else
                {
                    printf("Characters must be only letters\n");
                    return 3;
                }
            }
        }
        else
        {
            printf("Key must be 26 characters long\n");
            return 2;
        }
    }
    else
    {
        printf("Useage: ./substitution key\n");
        return 1;
    }
    // printf("key correct\n");
    return 0;
}

string subText(string text, string code, int length)
{
    int n = strlen(text);

    for (int i = 0, c = 0; i < n; i++)
    {
        if (isalpha(text[i]))
        {
            if (islower(text[i]))
            {
                text[i] = toupper(text[i]);
                c = 1;
            }
            int index = text[i] - 65;
            text[i] = code[index];
            if (c == 1)
            {
                text[i] = tolower(text[i]);
                c = 0;
            }
        }
        elsec
        {
            ;
        }
    }
    return text;
}