#include <stdio.h>

int main(){
    double p1[3][3];
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            scanf("%lf", &p1[i][j]);
        }
    }
    if(p1[0][0] == p1[1][1] && p1[1][1] == p1[2][2] && p1[0][1] ==  p1[0][2] && p1[0][2] == p1[1][0] && p1[1][0] == p1[1][2] && p1[1][2] == p1[2][0] && p1[2][0] == p1[2][1] && p1[2][1] == 0.0){
        printf("This is a scalar matrix");
    }
    else{
        printf("This is not a scalar matrix");
    }
    return 0;
}