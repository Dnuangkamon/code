#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

struct Study
{
  char fname[61];
  char lname[61];
  char sex[10];
  int age;
  char ID[13];
  double grade;
};
int main()
{
  struct Study students[21];
  for (int i = 0; i < 20; i++)
  {
    scanf("%s %s %s %d %s %lf", students[i].fname, students[i].lname, students[i].sex, &students[i].age, students[i].ID, &students[i].grade);
  }
  char channel[10];
  scanf("%s", channel);
  for (int i = 0; i < strlen(channel); i++)
  {
    channel[i] = tolower(channel[i]);
  }
  for (int i = 0; i < 20; i++)
  {
    for (int j = i; j < 20; j++)
    {
      if ((strcmp(channel, "name") == 0 && strcmp(students[i].fname, students[j].fname) > 0) || (strcmp(channel, "surname") == 0 && strcmp(students[i].lname, students[j].lname) > 0) || (strcmp(channel, "id") == 0 && strcmp(students[i].ID, students[j].ID) > 0))
      {
        struct Study ans_1 = students[i];
        students[i] = students[j];
        students[j] = ans_1;
      }
    }
  }
  for (int i = 0; i < 20; i++)
  {
    if (strcmp(students[i].sex, "Male") == 0)
    {
      strcpy(students[i].sex, "Mr");
    }
    else
    {
      strcpy(students[i].sex, "Miss");
    }
    printf("%s %c %s (%d) ID: %s GPA %.2lf\n",students[i].sex, students[i].fname[0], students[i].lname, students[i].age, students[i].ID, students[i].grade);
  }
  return 0;
}
