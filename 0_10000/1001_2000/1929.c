#include <math.h>
#include <stdio.h>

int main(){
    int start, end;

    scanf("%d %d", &start, &end);


    for (int i = start; i <= end; i++){
        if (i == 1) continue;
        else if (i == 2 || i == 3){
            printf("%d\n", i);
        }
        else{
            int j = 2;
            for (;j <= (int)sqrt((float)i) + 1; j++){
                if (i % j == 0){
                    break;
                }
            }
            if (j == (int)sqrt((float)i) + 2){
                printf("%d\n", i);
            }
        }
    }

}

