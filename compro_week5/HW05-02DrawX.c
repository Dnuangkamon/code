#include<stdio.h>

int main(){
    int i, j,i1, i2=0, i3=0, i4=0;
    scanf("%d", &i1);
    int i5=i1+1;
    for (i = 1; i < i1+1; ++i) {
        ++i2;
        ++i4;
        --i5;
        for(j = 1; j <= i1; ++j){
            if(j == i4 || j == i5){
                printf("-");
            }
            else{
                printf("#");
            }
        }
        printf("\n");
   }
}
