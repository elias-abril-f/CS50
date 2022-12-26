#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;
int tabulateCounter = 0;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // store the votes. cycle though the candidates names. If the vote and the
    // candidate's name are the same, store c which is the index
    for (int c = 0, n = candidate_count; c < n; c++)
    {
        if (strcmp(name, candidates[c].name) == 0)
        {
            preferences[voter][rank] = c;
            // printf("voted for %s\n", candidates[c].name);
            return true;
        }
        else
        {
            ;
        }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{

    // printf("tabulateCounter is %i\n", tabulateCounter);
    if (tabulateCounter > candidate_count)
    {
        return;
    }
    for (int i = 0; i < voter_count; i++)
    {
        // cycle though the [tabulateCounter]th choice of the voters
        if (candidates[preferences[i][tabulateCounter]].eliminated == false)
        {
            candidates[preferences[i][tabulateCounter]].votes++;
            printf("i is %i\n", i);
            printf("candidate[%i].votes is %i\n", preferences[i][tabulateCounter], candidates[preferences[i][tabulateCounter]].votes);
        }
        else
        {
            int tabulateCounterBackup = tabulateCounter;
            do
            {
                tabulateCounter++;
            }
            while (candidates[preferences[i][tabulateCounter]].eliminated == true);
            candidates[preferences[i][tabulateCounter]].votes++;
            printf("i is %i\n", i);
            printf("candidate[%i].votes is %i\n", preferences[i][tabulateCounter], candidates[preferences[i][tabulateCounter]].votes);
            tabulateCounter = tabulateCounterBackup;
        }
    }
    tabulateCounter++; // to select only one ranking at a time.
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    int tempMax = 0;
    int tie = 0;
    int index = -1;
    for (int i = 0; i < candidate_count; i++)
    {
        if (i == 0)
        {
            tempMax = candidates[i].votes;
        }
        if (candidates[i].votes > tempMax && candidates[i].eliminated == false)
        {
            tempMax = candidates[i].votes;
        }
    }
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == tempMax && candidates[i].eliminated == false)
        {
            tie++;
            index = i;
        }
    }
    if (tie == 1 && candidates[index].votes > voter_count / 2)
    {
        printf("%s\n", candidates[index].name);
        return true;
    }
    else
    {
        return false;
    }
}
// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    int tempMin = 0;
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (i == 0 && candidates[i].eliminated == false)
        {
            tempMin = candidates[i].votes;
        }
        if (candidates[i].votes < tempMin && candidates[i].eliminated == false)
        {
            tempMin = candidates[i].votes;
        }
    }
    return tempMin;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    int tieCheck = -1;
    int tie = 0;
    int candidatesLeft = candidate_count;

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].eliminated == true)
        {
            candidatesLeft--;
        }
    }
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].eliminated == false)
        {
            tieCheck = candidates[i].votes;
            break;
        }
    }
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == tieCheck && candidates[i].eliminated == false)
        {
            tie++;
        }
    }
    if (tie == candidatesLeft)
    {
        return true;
    }
    else
    {
        return false;
    }
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == min && candidates[i].eliminated == false)
        {
            candidates[i].eliminated = true;
        }
    }
    return;
}