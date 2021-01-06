#include <iostream>
#include <cstdio>

using namespace std;

int** arr;

void DFS(int n, int size){
  
  int idx = 0;
  while (idx != size){
    
    if (arr[n][idx] > 0){
      arr[n][idx]--;
      arr[idx][n]--;
      DFS(idx, size);
    }
    if (arr[n][idx] == 0){
      idx++;
    }
  }
  printf("%d ", n + 1);
}

int main(){

  int size = 0;
  scanf("%d", &size);
  arr = new int*[size];
  bool possible = true;
  for (int i = 0; i < size; i++){
    arr[i] = new int[size];
    int sum = 0;
    for (int j = 0; j < size; j++){
      scanf("%d", &arr[i][j]);
      sum += arr[i][j];
    }
    if (sum % 2 == 1){
      possible = false;
    }
  }

  if (possible){
    DFS(0, size);
    printf("\n");
  }
  else{
    printf("%d\n", -1);
  }
}
