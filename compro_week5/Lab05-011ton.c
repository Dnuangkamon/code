#include<stdio.h>

int main(){
    int i2 = 1;
    int i1 = 1;
    scanf("%d", &i2);
    while (i1 != i2+1) {
    printf("%d ", i1);
    ++i1;
  }
  return 0;
}
