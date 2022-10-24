#include<stdio.h>

int main(){
    int i, age, hig, wei, c1 =0, c2=0, c3=0, c4=0, a1=0;
    float a2=0, a3=0;
    for (i = 1; i < 50+1; ++i){
        scanf("%d %d %d", &age, &hig, &wei);
        a1 = a1 + age;
        a2 = a2 + hig;
        a3 = a3 + wei;
        if (age >= 20 && hig >= 160){
            c1 = c1 + 1;
        }
        if(age < 20 && (hig <= 180 || wei >= 60)){
            c2 = c2 + 1;
        }
        if(age >= 30 && (wei >= 40 && wei <= 80)){
            c3 = c3 + 1;
        }
        if(age < 40 && (wei < 85 || hig <= 200)){
            c4 = c4 + 1;
        }

    }
    printf("Age >= 20 and Height >= 160: %d\n", c1);
    printf("Age < 20 and Height <= 180 or Weight >= 60: %d\n", c2);
    printf("Age >= 30 and Weight >= 40 and Weight <= 80: %d\n", c3);
    printf("Age < 40 and Weight < 85 or Height <= 200: %d\n", c4);
    printf("Average Age: %d\n", a1/50);
    printf("Average Height: %.2f\n", a2/50);
    printf("Average Weight: %.2f\n", a3/50);
  return 0;
}