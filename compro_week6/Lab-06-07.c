//╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗

#include <stdio.h>
#include <ctype.h>

int main()
{
    char array1[26] = "KDECNMRQPYXBAIWGZVFUTHSOJL", array2[26] = "kdecnmrqpyxbaiwgzvfuthsojl", p1[201];
    scanf("%[^\n]", p1);
    for (int i = 0; p1[i] != '\0'; i++)
    {
        if (p1[i] >= 65 && p1[i] <= 90)
        {
            int p2;
            for (int j = 0; j < 26; j++)
            {
                if (p1[i] == array1[j])
                {
                    p2 = j;
                }
            }
            int new_p2 = p2 + 5;
            printf("%c", array1[new_p2%26]);
        }
        else if (p1[i] == 32)
        {
            printf(" ");
        }
        else
        {
            int p2;
            for (int j = 0; j < 26; j++)
            {
                if (p1[i] == array2[j])
                {
                    p2 = j;
                }
            }
            int new_p2 = p2 + 5;
            printf("%c", array2[new_p2%26]);
        }
    }
    return 0;
}
//╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝