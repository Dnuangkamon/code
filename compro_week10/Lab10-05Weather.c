#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

struct Weather
{
    char outlook[9]; // outlook{overcast,sunny,rain}
    int temperature;
    int humidity;
    char wind; // wind{T,F}
};

void playing_decision(struct Weather happy);

int main()
{
    int num;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        struct Weather happy;
        scanf("%s %d %d %c", &happy.outlook, &happy.temperature, &happy.humidity, &happy.wind);
        playing_decision(happy);
    }
    return 0;
}
void playing_decision(struct Weather happy)
{
    if (strcmp(happy.outlook, "overcast") == 0)
    {
        printf("yes\n");
    }
    else if (strcmp(happy.outlook, "rain") == 0)
    {
        if (happy.wind == 'F')
        {
            printf("yes\n");
        }
        else
        {
            printf("no\n");
        }
    }
    else if (strcmp(happy.outlook, "sunny") == 0)
    {
        if (happy.humidity <= 77.5)
        {
            printf("yes\n");
        }
        else
        {
            printf("no\n");
        }
    } 
}