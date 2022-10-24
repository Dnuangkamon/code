#include<stdio.h>

int main(){
    int i1,i2;
    scanf("%d %d", &i1, &i2);
    if(i1 > i2){
        while (i1 != i2-1) {
        printf("%d ", i1);
        --i1;
        }
    }
    else{
        while (i2+1 != i1) {
        printf("%d ", i1);
        ++i1;
        }
    }

  return 0;
}
