#include<stdio.h>
#include<string.h>
#include <ctype.h> 
int main(){
    char txt1[151],txt2[151],txt3[5] = " ";
    int count = 0;
    scanf("%s\n %[^\n]", &txt1, &txt2);
    txt1[0] = tolower(txt1[0]);
    for (int i = 0;i < strlen(txt2); i++){
        if((txt1[0] == txt3[0]) && (txt2[i] == txt3[0])){
            count += 1;
        }
        txt2[i] = tolower(txt2[i]);
        if(txt1[0] == txt2[i]){
            count += 1;
        }
    }
    printf("%d", count);
}