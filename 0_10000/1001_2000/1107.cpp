#include <iostream>
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define ABS(a) (((a) < (0)) ? (-a) : (a))

using namespace std;

int is_broken(int* arr, int num){
  int ret_val = 0;
  while (num != 0){
    if (arr[num % 10]) {
      ret_val = 1;
      break;
    }
    num /= 10;
  }
  return ret_val;
}

int main(){
  int arr[10] = {0, };
  int target = 0;
  int ans1 = 0, ans2 = 0;
  int num1 = 0, num2 = 0;
  int len_broken = 0;

  cin >> target;
  num1 = target;
  num2 = target;
  cin >> len_broken;

  for (int i = 0; i < len_broken; i++){
    int tmp = 0;
    cin >> tmp;
    arr[tmp] = 1;
  }

  while (1){
    if (num1 == 100){
      break;
    }
    else if (is_broken(arr, num1)){
      num1++;
      ans1++;
    }
    else if (num1 > 999900){
      ans1 = 1000000;
      break;
    }
    else{
      break;
    }
  }
  while (1){
    if (num2 == 100){
      break;
    }
    else if (is_broken(arr, num2)){
      num2--;
      ans2++;
    }
    else if (num2 < 0){
      ans2 = 1000000;
      break;
    }
    else{
      break;
    }
  }

  if (num1 < 98 || num1 > 102){
    while (num1 != 0){
      ans1++;
      num1 /= 10;
    }
  }
  else{
    int tmp = ABS(num1 - 100);
    ans1 += tmp;
  }
  if (num2 < 98 || num2 > 102){
    while (num2 != 0){
      ans2++;
      num2 /= 10;
    }
  }
  else{
    int tmp = ABS(num2 - 100);
    ans2 += tmp;
  }

  cout << MIN(ans1, ans2) << endl;
}
