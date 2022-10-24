#include<stdio.h>

int main(){
    int i1,i2;
    scanf("%d", &i1);
    if(i1 > 0){
        while (i1 != 0-1) {
        printf("%d ", i1);
        --i1;
        }
    }
    else{
        while (i1 != 0+1) {
        printf("%d ", i1);
        ++i1;
        }
    }

  return 0;
}
