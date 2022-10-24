#include<stdio.h>

int main(){
    int i1, i2 = 0;
    scanf("%d", &i1);
    while (i1 != -9) {
        i2 += i1;
        scanf("%d", &i1);
  }
  printf("%d", i2);
  return 0;
}