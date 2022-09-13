#include<stdio.h>  
void main ()  
{  
    int a[10] = {100, 206, 300, 409, 509, 601}; //Line 1  
    int *p[] = {a, a+1, a+2, a+3, a+4, a+5}; //Line 2  
    int **pp = p; //Line 3  
    pp++; // Line 4  
    printf("%d %d %d\n",pp-p,*pp - a,**pp); // Line 5  
    *pp++; // Line 6  
    printf("%d %d %d\n",pp-p,*pp - a,**pp); // Line 7  
    ++*pp; // Line 8  
    printf("%d %d %d\n",pp-p,*pp - a,**pp); // Line 9  
    ++**pp; // Line 10   
    printf("%d %d %d\n",pp-p,*pp - a,**pp); // Line 11  
}  