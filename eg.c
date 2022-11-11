#include <stdio.h>

int main()
{
    char buffer[1024];
    FILE *fptr = fopen("text.txt", "r");
    if (fptr == NULL) 
    {
            printf("failed to open text.txt");
    }
    fscanf(fptr, "%[^\n]", buffer);
    printf("Read data: %s\n", buffer);
}
