#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");


    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    if (score1 > score2) printf("Player 1 wins!\n");
    else if (score1 < score2) printf("Player 2 wins!\n");
    else printf("Tie!\n");
}

int compute_score(string word)
{
    int totalPoints = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        //convert to upper letters and substract 64 to the ascii code to obtain the alphabetical order. A = 65 minus 64 -> 1
        if (isalpha(word[i])) word[i] = toupper(word[i]) - 64;

        // use the ascii code as an integer instead of a character. -1 because POINTS is an array so its 0 indexed so from now on A = 0
        totalPoints += POINTS[ word[i] - 1];
    }
    return totalPoints;
}
