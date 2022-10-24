#include<stdio.h>
#include<string.h>
#include <ctype.h> 
int main(){
    char txt1[255],txt2[5] = " ";
    scanf("%[^\n]", &txt1);
    for (int i = 0;i < strlen(txt1); i++){
       if(txt1[i] == txt2[0]){
           continue;
       }
       printf("%c",txt1[i]);
    }
    
}