#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char tag[50], html_tag[10000], tag_close[2] = "<";
    const char txt[1000];
    char tag_html[50] = "</html>";
    int count = 0;
    while(1) {
        scanf("%s", &txt);
        strcat(html_tag, txt);
        if (strstr(txt, tag_html) != NULL) {
            break;
        }
    }
    
    scanf("%s", tag);
    int check = 0;
    
    for (int i = 0; i < strlen(html_tag); i++) {
        if (html_tag[i+1] == tag[0] && html_tag[i+2] == tag[1]) {
            
            count = i + strlen(tag)+2;
            
            
            for (int j = count; j < strlen(html_tag); j++) {
                
                if (html_tag[j] == tag_close[0]) {
                    check = 1;
                    break;
                }
                
                else if(check){
                    printf("\n");
                    check = 0;
                }
                printf("%c", html_tag[j]);
            }
        }
    }
    return 0;
}