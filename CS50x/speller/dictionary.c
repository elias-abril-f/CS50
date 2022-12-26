// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 187751;

// Hash table
node *table[N];

unsigned int wordCount = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Hash the word to find out which bucket to scan
    int h = hash(word);
    // Create a temp node to use as a cursor
    node *temp = table[h];

    // If that position is not empty, compare the word field with out word, if equal is spelled correctly, return true
    while (temp != NULL)
    {
        if (strcasecmp(word, temp->word) == 0)
        {
            return true;
        }
        // if not equal, move the cursor to the next node in the list of this bucket and try again
        temp = temp->next;
    }
    // if the word is not equal to any of the words stored in the nodes linked withing the bucket corresponding to the hash, must be false
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // long just in case we go over 2 billion, as we can only use positives.
    long hash = 0;
    // for every letter in the word, convert to lower as it'll give a higher number. Multiply by 31 as its prime
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        hash += tolower(word[i]) * 31;
    }
    // return the reminder of the hash by the number of buckets to make sure the hash is not bigger than the amount of buckets
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Loads the dictionary file provided by the pointer *dictionary
    FILE *input = fopen(dictionary, "r");

    // If the dictionary can't be opened return false
    if (input == NULL)
    {
        return false;
    }

    // Create a buffer to be used in the fscanf function
    char *buffer = malloc(LENGTH + 1);
    if (buffer == NULL)
    {
        return false;
    }

    // Using fscanf read each word in the dictionary file and store it in the buffer
    while (fscanf(input, "%s", buffer) == 1)
    {
        // Using malloc, create new memory for the new node where the word in buffer will be stored
        node *newNode = malloc(sizeof(node));

        // If we couldn't get any memory from malloc, return false
        if (newNode == NULL)
        {
            return false;
        }
        // If we got memory from malloc, copy from the buffer to the word field of the new node
        strcpy(newNode->word, buffer);

        // Create the hash that will be used to store the new word by calling the hash() function
        int h = hash(buffer);

        // Create the head node to check if that specific index in the table, table[hash] is empty

        if (table[h] == NULL)
        {
            // if empty then the fist node on that index will be our current node
            newNode->next = NULL;
            table[h] = newNode;
            wordCount++;
        }
        else
        {
            // if not empty, our current node's "next" field, newNode->next, is copied into the head of the existing list in that node
            newNode->next = table[h];
            //then the current node is made into the head of the list
            table[h] = newNode;
            // added one to the word count
            wordCount++;
        }
    }

    // Close the dictionary file
    free(buffer);
    fclose(input);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return wordCount++;
}


// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // for every bucket
    for (int i = 0; i <= N; i++)
    {
        // while the bucket in question is not empty
        while (table[i] != NULL)
        {
            // copy the pointer to the next item in the list to a temp node
            node *tmp = table[i]->next;
            // free the current node
            free(table[i]);
            // make our current node the same as the temp, which means, make our current node the next in the list and start again
            table[i] = tmp;
        }
    }
    return true;
}