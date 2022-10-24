#include <stdio.h>
#include <string.h>

int main()
{
    char text1[30], text2[30];
    scanf("%s\n%s", &text1, &text2);

    if (strcmp(text1, "Rock") == 0)
    {

        if (strcmp(text2, "Scissors") == 0)
        {
            printf("Win");
        }
        else if (strcmp(text2, "Paper") == 0)
        {
            printf("Lose");
        }
        else if (strcmp(text2, "Rock") == 0)
        {
            printf("Draw");
        }
        else
        {
            printf("Error");
        }
    }
    else if (strcmp(text1, "Scissors") == 0)
    {
        if (strcmp(text2, "Paper") == 0)
        {
            printf("Win");
        }
        else if (strcmp(text2, "Rock") == 0)
        {
            printf("Lose");
        }
        else if (strcmp(text2, "Scissors") == 0)
        {
            printf("Draw");
        }
        else
        {
            printf("Error");
        }
    }

    else if (strcmp(text1, "Paper") == 0)
    {
        if (strcmp(text2, "Rock") == 0)
        {
            printf("Win");
        }
        else if (strcmp(text2, "Scissors") == 0)
        {
            printf("Lose");
        }
        else if (strcmp(text2, "Paper") == 0)
        {
            printf("Draw");
        }
        else
        {
            printf("Error");
        }
    } 
    else {
        printf("Error");
    }
    

    return 0;
}