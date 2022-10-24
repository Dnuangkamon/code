#include <stdio.h>
#include <ctype.h>
#include <string.h>


int main() {
    char list_name[200][200], sorted[200];

    //input array[i][j]
    for (int i = 0; i < 20; i++) {
        scanf(" %[^\n]", &list_name[i]);
        for (int j = 0; j < strlen(list_name[i]); j++) {
            if (j == 0 || list_name[i][j-1] == " "[0]){
                char upper = toupper(list_name[i][j]);
                list_name[i][j] = upper;
            }
            else{
                char lower = tolower(list_name[i][j]);
                list_name[i][j] = lower;
            }
        }
    }

    /// sorted
    for (int i = 0; i < 20; i++) {
        for (int j = 0; j < 20-1-i; j++) {
            // compare
            if (strcmp(list_name[j], list_name[j+1]) > 0) {
                strcpy(sorted, list_name[j+1]);
                strcpy(list_name[j+1], list_name[j]);
                strcpy(list_name[j], sorted);
            }
        }
    }
    
    //output
    for (int i = 0; i < 20; i++) {
        printf("%s\n", list_name[i]);
    }
    return 0;
}
