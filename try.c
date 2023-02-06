#include<stdio.h>

int main(){
    int a;
    int b;
    int c;
    scanf("%d %d",&a, &b);
    printf("gcd of %d ,%d is\n",a,b);
    while (!(b==0)){
        c = a;
        a = b;
        b = c % b;
    }
    printf("%d\n", a);
    return 0;
}