
#include <stdio.h>

/*
 * This is the brute force solution
 */
int main(char* args)
{

    int MAX_VALUE = 1000;

    int total = 0;
    for (int i = 3; i < MAX_VALUE; i++) 
    {
        if (i % 3 == 0 || i % 5 == 0) 
        {
            total += i;
        }
    }

    printf("%d\n", total);

    return 0;
}