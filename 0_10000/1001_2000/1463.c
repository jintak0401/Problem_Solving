#include <stdio.h>

int arr[1000001] = {0, 0, 1, 1, 0, };


int main(){
    int num = 0;

    scanf("%d", &num);

    for (int i = 4; i <= num; i++){
        int tmp[3] = {9999999, 9999999, 9999999};
        if (i % 3 == 0){
            tmp[0] = arr[i / 3];
        }
        if (i % 2 == 0){
            tmp[1] = arr[i / 2];
        }

        tmp[2] = arr[i - 1];

        arr[i] = (tmp[0] > tmp[1] ? tmp[1] : tmp[0]);
        arr[i] = (arr[i] > tmp[2]) ? tmp[2] : arr[i];
        arr[i]++;
    }

    printf("%d\n", arr[num]);

}
