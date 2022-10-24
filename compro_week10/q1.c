/******************************************************************************
Name: Tanathip Singhanon
Student ID: 64070045
*******************************************************************************/
#include<stdio.h>
#include<string.h>
#include <ctype.h> 

void swap(double *a, double *b, double *c) {
    double temp;
    if (*c < *b) {
        temp = *b;
        *b = *c;
        *c = temp;
    }
    if (*b < *a) {
        temp = *a;
        *a = *b;
        *b = temp;
    }
    if (*c < *b) {
        temp = *b;
        *b = *c;
        *c = temp;
    }
}

int main() {
    double n1, n2, n3;
    scanf("%lf %lf %lf", &n1, &n2, &n3);
    swap(&n1, &n2, &n3);
    printf("%.5lf\n%.5lf\n%.5lf\n", n1, n2, n3);
    return 0;
}