#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <stdint.h>

typedef uint8_t BYTE;
const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    if (argv[1] == NULL)
    {
        printf("Could not open file.\n");
        return 2;
    }
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open file\n");
        return 3;
    }

    int counter = 0;
    BYTE buffer[BLOCK_SIZE];
    FILE *output = NULL;
    char outputname[8];

    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        if ((buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff) && (buffer[3] >= 0xe0 && buffer[3] <= 0xef))
        {
            // if this is not the first photo found, close the previous one
            if (!(counter == 0))
            {
                fclose(output);
            }
            // print the output name to a string
            //%03i for printing leading zeroes up to 3 digits.
            sprintf(outputname, "%03i.jpg", counter);

            // open a file (create) with that name
            output = fopen(outputname, "w");

            // add one to the counter for the naming the next photo found
            counter++;
        }
        if (!(counter == 0))
        {
            // write to the output file
            fwrite(buffer, 1, BLOCK_SIZE, output);
        }
    }
    fclose(file);
    fclose(output);
    return 0;
}