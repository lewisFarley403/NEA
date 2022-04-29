#include <stdio.h>
int main(){
    char str1[20];
    int y=0;
    for (int i =0;i<9000000000000000000;i++){
        y+=i;
    }
    printf("%d",y);
    scanf("%19s",str1);
    return 0;
}