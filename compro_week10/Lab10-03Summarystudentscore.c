#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct student
{
  char firstname[100];
  char lastname[100];
  int midterm;
  int final;
  int assignment;
  int total;
} students[10];
int checkScore(struct student student);

void printScore(struct student students[], int amount);

int main()
{
  int aaa, nums, ans_1;
  for (int i = 0; i < 10; i++)
  {
    scanf("%s", &students[i].firstname);
    if (strcmp(students[i].firstname, "END") == 0)
    {
      nums = i;
      break;
    }
    scanf("%s %d %d %d %d", &students[i].lastname, &students[i].midterm, &students[i].final, &students[i].assignment, 0);
    aaa = students[i].midterm + students[i].final + students[i].assignment;
    students[i].total = aaa;

    aaa = checkScore(students[i]);
    if (aaa == 9999)
    {
      ans_1 = 1150;
      i -= 1;
      printf("Error\n");
    }
  }

  printf("1234567890123456789012345678901234567890\n");

  printf("M    F    A    TT\n");

  for (int i = 0; i < nums; i++)
  {
    aaa = checkScore(students[i]);
    if (aaa == 1)
    {
      printf("%c %s        %d   %d   %d   %d\n", students[i].firstname[0], students[i].lastname, students[i].midterm, students[i].final, students[i].assignment, students[i].total);
    }
  }
}

int checkScore(struct student student)
{
  if (student.total <= 100 && student.total >= 0 && (student.midterm <= 100 && student.midterm >= 0) && (student.final <= 100 && student.final >= 0) && (student.assignment <= 100 && student.assignment >= 0))
  { // check ทุกตัว ที่้เกิน 100
    return 1;
  }
  else
  {
    return 9999;
  }
};


// Sawasdee Khunkru 20 30 15
// Hello World 100 29 100
// Hello World 101 29 39
// END

// Sawasdee Khunkru 20 30 15
// Hello World 21 29 100
// Hello World 21 29 39
// END