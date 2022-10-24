#include<stdio.h>
#include<string.h>
#include <ctype.h> 
int main(){
    int check=1,i1,j,count[500]={};
    char input2,input,colect[500]={};
    scanf("%d", &i1);
    for(int i=0;i<i1;i++){
        scanf("\n%c", &input);
        input2 = tolower(input);
        for(j=0;j<strlen(colect);j++){
            if(colect[j]==input2){
                count[j]+= 1;
                check=0;
                break;
            }
        }
        if(check == 1){
            colect[j] = input2;
            count[j] = 1;
        }
        check=1;
    }
        for(int i = 0;i<strlen(colect);i++){
            printf("%c: %d\n", colect[i], count[i]);
        }
}