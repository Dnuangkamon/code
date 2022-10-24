#include<stdio.h>

int main(){
    int i1;
    scanf("%d", &i1);
    if(i1 == 1){
        printf("Sunday");
    }
    else if(i1 == 2){
        printf("Monday");
    }
    else if(i1 == 3){
        printf("Tuesday");
    }
    else if(i1 == 4){
        printf("Wednesday");
    }
    else if(i1 == 5){
        printf("Thursday");
    }
    else if(i1 == 6){
        printf("Friday");
    }
    else if(i1 == 7){
        printf("Saturday");
    }
    else{
        printf("Error");
    }
    return 0;
}