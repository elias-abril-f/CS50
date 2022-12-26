#include "helpers.h"
#include <math.h>

// Convert image to grayscale
//  all the values for R G B are the average of all the colours for that pixel.
// newRed =  (oldRed + oldGreen + oldBlue) / 3.0(so the result is a float) and round the result.
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // loop to select the row
    for (int i = 0, h = height, w = width, newValue = 0; i < h; i++)
    {
        // loop to select the column inside the selected row -> specific pixel
        for (int j = 0; j < w; j++)
        {
            newValue = round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0);
            image[i][j].rgbtRed = newValue;
            image[i][j].rgbtBlue = newValue;
            image[i][j].rgbtGreen = newValue;
            newValue = 0;
        }
    }
    return;
}

// Convert image to sepia
// sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
// sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
// sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue

void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0, h = height, w = width, newValue = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            int Red = image[i][j].rgbtRed;
            int Green = image[i][j].rgbtGreen;
            int Blue = image[i][j].rgbtBlue;
            // newRed
            if (.393 * Red + .769 * Green + .189 * Blue <= 255)
            {
                image[i][j].rgbtRed = round(.393 * Red + .769 * Green + .189 * Blue);
            }
            else
            {
                image[i][j].rgbtRed = 255;
            }

            // newGreen
            if (.349 * Red + .686 * Green + .168 * Blue <= 255)
            {
                image[i][j].rgbtGreen = round(.349 * Red + .686 * Green + .168 * Blue);
            }
            else
            {
                image[i][j].rgbtGreen = 255;
            }

            // newBlue
            if (.272 * Red + .534 * Green + .131 * Blue <= 255)
            {
                image[i][j].rgbtBlue = round(.272 * Red + .534 * Green + .131 * Blue);
            }
            else
            {
                image[i][j].rgbtBlue = 255;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE buffer;
    for (int i = 0, h = height, w = width; i < h; i++)
    {
        // n is equal to the width of the row to select the last pixel and it counts down.
        // that way 0 gets swaped with the last one, 1 witht last - 1, 2 with last - 2, etc...
        for (int j = 0, n = w - 1; j < n; j++, n--)
        {

            buffer = image[i][j];
            image[i][j] = image[i][n];
            image[i][n] = buffer;
        }
    }
    return;
}
//////////////////////////////////WORKING UP TO HERE/////////////////////////////////////////////////////////
// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    // copy image to make sure blured pixels dont affect the rest
    RGBTRIPLE copy[height][width];
    for (int i = 0, h = height, w = width, newValue = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    // row loop
    for (int i = 0; i < height; i++)
    {
        // column loop
        for (int j = 0; j < width; j++)
        {
            int bufferRed = 0;
            int bufferGreen = 0;
            int bufferBlue = 0;
            float divider = 0.0;

            for (int r = -1; r < 2; r++)
            {
                for (int c = -1; c < 2; c++)
                {
                    // if when adding or removing 1 to the current pixel we go past the first of last row, skip the loop this time
                    if (i + r < 0 || i + r > height - 1)
                    {
                        continue;
                    }
                    // if when adding or removing 1 to the current pixel we go past the first of last column, skip the loop this time
                    if (j + c < 0 || j + c > width - 1)
                    {
                        continue;
                    }
                    // if when taking or adding 1 column or row to the current pixel we are still within the image, add to the buffer
                    //  and add 1 to the divider so we can do the average.
                    bufferRed += copy[i + r][j + c].rgbtRed;
                    bufferGreen += copy[i + r][j + c].rgbtGreen;
                    bufferBlue += copy[i + r][j + c].rgbtBlue;
                    divider++;
                }
            }

            image[i][j].rgbtRed = round(bufferRed / divider);
            image[i][j].rgbtGreen = round(bufferGreen / divider);
            image[i][j].rgbtBlue = round(bufferBlue / divider);
        }
    }
    return;
}
