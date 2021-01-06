#include <cstdio>
#include <iostream>
#define MIN(a, b)  (((a) < (b)) ? (a) : (b))

void printing(int* ans){
  for (int i = 0; i < 6; i++){
    printf("%d  ", ans[i]);
  }
  printf("\n");
}

int main(){
  
  int house_num;
  scanf("%d", &house_num);
  int** price = new int*[house_num];
  for (int i = 0; i < house_num; i++){
    price[i] = new int[3];
    for (int j = 0; j < 3; j++){
      scanf("%d", &price[i][j]);
    }
  }
  int ans[3] = {price[0][0], price[0][1], price[0][2]};
  int tmp[3];
  for (int i = 1; i < house_num; i++){
    tmp[0] = MIN(ans[1] + price[i][0], ans[2] + price[i][0]);
    tmp[1] = MIN(ans[0] + price[i][1], ans[2] + price[i][1]);
    tmp[2] = MIN(ans[0] + price[i][2], ans[1] + price[i][2]);
    ans[0] = tmp[0];
    ans[1] = tmp[1];
    ans[2] = tmp[2];
  }
  int min = MIN(ans[0], ans[1]);
  min = MIN(min, ans[2]);
  printf("%d\n", min);
}
