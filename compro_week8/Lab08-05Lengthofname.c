#include<stdio.h>
#include<string.h>
#include <ctype.h> 

int main(){
    char txt1[255], txt2[255];
    scanf("%[^\n] %[^\n]", txt1, txt2);
    if(strlen(txt1) > strlen(txt2)){
        printf("%s", txt1);
    }
    else if(strlen(txt1) < strlen(txt2)){
        printf("%s", txt2);
    }
    else{
        printf("\\7");
    }
    return 0;
}