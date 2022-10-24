/******************************************************************************
Name: Tanathip Singhanon
Student ID: 64070045
*******************************************************************************/
#include <stdio.h>

int main(){
    char i1;
    scanf("%c", &i1);
    if(i1 >= 97 && i1 <= 122){
        for(int i = 97; i <= i1; i++)
        {
            printf("%c ", i);
        }
    }else{
        printf("Error");
    }
    return 0;
}