/******************************************************************************
Name: Tanathip Singhanon
Student ID: 64070045
*******************************************************************************/
#include <stdio.h>

int main(){
    int i1, i2;
    scanf("%d %d", &i1, &i2);
    if (i1 < 1 || i2 < 1)
    {
        printf("Error");
    }
    for (int i = 1; i < i2 + 1; i++)
    {
        printf("%dx%d=%d\n", i1, i, i1 * i);
    }
    return 0;
}