#include <stdio.h>

int main() {
   int i1, i2, i3, i4 = 0;
   scanf("%d", &i3);
   for (i1 = 1; i1 <= i3; ++i1, i4=0) {
      for (i2 = 1;i2 <= i3-i1;++i2) {
         printf(" ");
      }
      while (i4 != 2*i1-1) {
         printf("*");
         ++i4;
      }
      printf("\n");
   }
   return 0;
}