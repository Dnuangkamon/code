#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int main()
{
    char txt1[255], txt3[255] = " ";
    int count = 0;
    scanf("%[^\n]", txt1);
     for (int i = 0;i < strlen(txt1); i++){
       if(txt1[i] == txt3[0]){
           count += 1;
       }
    }
    printf("%d words\n", count+1);
    printf("----\n");
    char *txt2 = strtok(txt1, " ");
    while (txt2 != NULL)
    {
        for(int i = 0; i< strlen(txt2); i++)
        {
            printf("%c", tolower(txt2[i]));
        }
        printf(" : %d", strlen(txt2));
        printf("\n");
        txt2 = strtok(NULL, " ");
    }

    return 0;
}