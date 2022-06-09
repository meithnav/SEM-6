#include<stdio.h> 
#include<string.h>

# define MAX_LEN 10

int main(){

    char name[MAX_LEN]; char new_name[MAX_LEN];
    char list_names[3][MAX_LEN] = {{"Meith"} , {"IS Pract"} , {"Testing 1"}};
    printf("\nENTER NAME : ");


    // gets(name);
    fgets(name, MAX_LEN , stdin);
    name[strcspn(name,"\r\n")]=0;

    int flag=0;
    for(int i=0; i<3; i++){
        if(flag ==1) break;
        if(strcmp(list_names[i], name) ==0 ){
            printf("\nENTER NEW NAME : ");

            // gets(new_name);
            fgets(new_name, MAX_LEN , stdin);
            new_name[strcspn(new_name,"\r\n")]=0;


            strcpy(&list_names[i][0],new_name); 

            printf("\nUPDATED LIST :");
            for(int j=0;j<3;j++) printf("\n%s",list_names[j]);
            flag=1;
        }
    }

    printf("\n\n");
    return 0;
}

