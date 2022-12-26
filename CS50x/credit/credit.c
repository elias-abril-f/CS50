#include <cs50.h>
#include <stdio.h>
#include <math.h>

// MASTERCARD: 16-Digit #'s, Start with: 51, 52, 53, 54, or 55
// VISA: 13-16-Digit #'s, Start with: 4
// AMEX: 15-Digit #'s, Start with: 34 or 37

// Luhn's Algorithm:
// 1. Multiply every other digit by 2, starting with the second number to the last
// 2. Add the sum of product's digits. Eg  if the digit is 6 multiply by 2 -> 12 would be 1+2
// 3. Add the sum of the other digits (not multiplied by 2)
// 4. If the total sum ends with a 0, it is valid!



int main(void)
{
    long cardNumber = get_long("Card's number: ");
    long cN = cardNumber;

    //length
    int length = 0;
    do
    {
        cN = cN / 10;
        length ++;
    }
    while (cN != 0);

    //Luhn algorith
    if (length != 13 && length != 15 && length != 16)
    {
        printf("INVALID\n");
        return 0;
    }
    // X is the numbers that are doubled
    int x;
    // Y is the numbers not doubled
    int y;
    int numbersDoubled = 0;
    int numbersNOTDoubled = 0;
    long newNumber = cardNumber;

    for (int i = 0; i < length / 2 + 1; i++)
    {
        y = newNumber % 10;
        //printf("Last number is: %i\n", y);
        numbersNOTDoubled +=  y;
        //printf("numbersNOTDoubled is: %i\n", numbersNOTDoubled);
        newNumber = newNumber / 10;
        //printf("Remaining is: %ld\n\n", newNumber);

        x = newNumber % 10;
        x = x * 2;
        //printf("Last number is: %i\n", x);
        if (x < 10)
        {
            numbersDoubled += x;
        }
        else
        {
            numbersDoubled += 1;
            numbersDoubled += x % 10;
        }

        //printf("numbersDoubled is: %i\n", numbersDoubled);
        newNumber = newNumber / 10;
        //printf("Remaining is: %ld\n\n", newNumber);
    }
    int totalSum = numbersDoubled + numbersNOTDoubled;
    //printf("card is valid\n");
    if (totalSum % 10 == 0 && length == 15)
    {
        int disposableLength = length - 2;
        long divider = pow(10, disposableLength);
        if ((cardNumber / divider) == 37 || (cardNumber / divider) == 34)
        {
            printf("AMEX\n");
            return 0;
        }
    }

    if ((totalSum % 10 == 0 && length == 13) || (totalSum % 10 == 0 && length == 16))
    {
        int disposableLength = length - 1;
        long divider = pow(10, disposableLength);
        if ((cardNumber / divider) == 4)
        {
            printf("VISA\n");
            return 0;
        }
    }

    if (totalSum % 10 == 0 && length == 16)
    {
        int disposableLength = length -2;
        long divider = pow(10, disposableLength);
        if ((cardNumber / divider) == 51 || (cardNumber / divider) == 52 || (cardNumber / divider) == 53 || (cardNumber / divider) == 54 ||
            (cardNumber / divider) == 55)
        {
            printf("MASTERCARD\n");
            return 0;
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}