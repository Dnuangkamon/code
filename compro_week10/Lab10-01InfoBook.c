#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
 
int main()
{
    struct student_info{
        char fname[20], sname[20], sex[20];
        int age, id;
        float gpa;
    }student;
    scanf("%s %s %s %d %d %f", &student.fname, &student.sname, &student.sex, &student.age, &student.id, &student.gpa);
    if(strcmp(student.sex,"Male") == 0){
        strcpy(student.sex, "Mr");
    }
    else{
        strcpy(student.sex, "Miss");
    }

    printf("%s %c %s (%d) ID: %d GPA %.2f", student.sex, student.fname[0], student.sname,student.age,student.id, student.gpa);
    return 0;
}