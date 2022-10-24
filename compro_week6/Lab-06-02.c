#include <stdio.h>

int main(){

    double i1,i2,i3;
    double i4,i5,i6;
    double i7,i8,i9;
    double j1,j2,j3;
    double j4,j5,j6;
    double j7,j8,j9;
    scanf("%lf %lf %lf",&i1,&i2,&i3);
    scanf("%lf %lf %lf",&i4,&i5,&i6);
    scanf("%lf %lf %lf",&i7,&i8,&i9);
    scanf("%lf %lf %lf",&j1,&j2,&j3);
    scanf("%lf %lf %lf",&j4,&j5,&j6);
    scanf("%lf %lf %lf",&j7,&j8,&j9);
    double ans1 = (i1*j1)+(i2*j4)+(i3*j7);
    double ans2 = (i1*j2)+(i2*j5)+(i3*j8);
    double ans3 = (i1*j3)+(i2*j6)+(i3*j9);
    double ans4 = (i4*j1)+(i5*j4)+(i6*j7);
    double ans5 = (i4*j2)+(i5*j5)+(i6*j8);
    double ans6 = (i4*j3)+(i5*j6)+(i6*j9);
    double ans7 = (i7*j1)+(i8*j4)+(i9*j7);
    double ans8 = (i7*j2)+(i8*j5)+(i9*j8);
    double ans9 = (i7*j3)+(i8*j6)+(i9*j9);
    printf("A x B\n");
    printf("%.2lf ",ans1);
    printf("%.2lf ",ans2);
    printf("%.2lf\n",ans3);
    printf("%.2lf ",ans4);
    printf("%.2lf ",ans5);
    printf("%.2lf\n",ans6);
    printf("%.2lf ",ans7);
    printf("%.2lf ",ans8);
    printf("%.2lf ",ans9);


    return 0;
}