#include <stdio.h>  

void calculate(){
    printf("Hello World\n");
    int x,y;
    char oper;
    printf("Enter num1: ");
    scanf("%d",&x);
    printf("Enter num2: ");
    scanf("%d",&y);
    printf("Enter operation: ");
    scanf("%s",&oper);

    if (oper == '+'){
        printf("Sum of %d and %d is %d",x,y,x+y);
    }
    else if (oper == '-'){
        printf("Difference of %d and %d is %d",x,y,x-y);
    }
    else if (oper == '/'){
        printf("Division of %d and %d is %d",x,y,x/y);
    }
    else if (oper == '*')
    {
        printf("Multiplication of %d and %d is %d",x,y,x*y);
    }
    else {
        printf("Invalid Operation");
    }
    printf("\n");

    }
int main(void){
    calculate();
    

}