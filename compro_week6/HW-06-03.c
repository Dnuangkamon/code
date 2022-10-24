#include<stdio.h>
#include<string.h>

int main(){
    char i1[100];
    int num=0;
    scanf("%[^\n]", i1);
    int i2 = strlen(i1)-1;
    int i3 = strlen(i1);
    for (int i = i2; i >= 0; i--)
    {
       if(i1[i] == i1[i2-i]){
           num += 1;
       }
    }
    if(num == i3){
        printf("It is Palindrome.");
    }
    else{
        printf("It is not Palindrome.");
    }
    return 0;
}