#include <stdio.h>
#include <ctype.h>
 
int main()
{
    char p1[301],p2;
    scanf("%[^\n] %c", &p1, &p2);
    int n1 = 0, n2 = 0, n3 = 0;
  //เช็ค
    for (int i = 0; p1[i] != '\0'; i++)
    {
        if (tolower(p1[i]) == p2)
        {
            n2++;
            n1 = 1;
        }
    }
    if (n1 == 0)
    {
        printf("Not found.");
    }
    else
    {
        printf("There is/are %d \"%c\" in the above sentences.\n", n2, p2);
        printf("Position:");
        for (int i = 0; p1[i] != '\0'; i++)
        {
            if (tolower(p1[i]) == p2)
            {
                //ใส่ลูกน้ำ
                if (n3 == 0)
                {
                    printf(" %d", i + 1);
                    n3 = 1;
                }
                else
                {
                    printf(", %d", i + 1);
                }
            }
        }
    }
    return 0;
}