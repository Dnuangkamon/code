#include <stdio.h>
#include<string.h>

int main(){
    char i1[100];
    scanf("%[^\n]", i1);
    int i2 = strlen(i1)-1;
    for (int i = i2; i >= 0; i--)
    {
        printf("%c", i1[i]);
    }
    return 0;
}