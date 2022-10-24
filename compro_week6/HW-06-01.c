#include <stdio.h>

int main()
{
    char i1[26] = "ZGWIABXYPQRMNCEDKLJOSHTUFV", i2[26] = "zgwiabxypqrmncedkljoshtufv", p1[201];
    int old;
    scanf("%[^\n]", p1);
    for (int i = 0; p1[i] != '\0'; i++)
    {
        if (p1[i] >= 65 && p1[i] <= 90)
        {
            for (int j = 0; j < 26; j++)
            {
                if (p1[i] == i1[j])
                {
                    old = j;
                }
            }
            int new = old + 5;
            printf("%c", i1[new % 26]);
        }
        else if (p1[i] == 32)
        {
            printf(" ");
        }
        else
        {
            int old;
            for (int j = 0; j < 26; j++)
            {
                if (p1[i] == i2[j])
                {
                    old = j;
                }
            }
            int new = old + 5;
            printf("%c", i2[new % 26]);
        }
    }
    return 0;
}