#include <stdio.h>



int main()
{   // array โจทย์
    int M[] = {2, 20, 8, 10, 4, 6, 16, 18};
    int N[] = {1, 3, 9, 7, 11, 15, 19};
    int num;
    while (1)
    {
        int num1;
        scanf("%d", &num1);
        for (int i = 1;i <= 20;i++)
        {
            if (num1 == i)
            {
                for (int j = 0;j <= 8;j++)
                {
                    if (num1 == M[j])
                    {
                        printf("%d is in M at index [%d]", num1, j);
                        num = 1;
                    }
                }
                for (int j = 0; j < 7; j++)
                {
                    if (num1 == N[j])
                    {
                        printf("%d is in N at index [%d]", num1, j);
                        num = 1;
                    }
                }
            
                if (num != 1)
                {
                    printf("%d is not in neither M nor N", num1);
                    num = 1;
                }
            }
        }
        //หยุด for
        if(num == 1)
        {
            break;
        }
    }
    return 0;
}