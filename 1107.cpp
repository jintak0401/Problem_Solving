#include <cstdio>
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define MAX(a, b) (((a) > (b)) ? (a) : (b))
#define ABS(a) (((a) < (0)) ? -(a) : (a))

int len(int num){

  if (num == 0){
    return 1;
  }

  int ret_val = 0;

  while (num != 0){
    ret_val += 1;
    num /= 10;
  }
  return ret_val;
}

int is_available(int* arr, int num){
  if (num == 0){
    if (arr[0]){
      return 0;
    }
    else{
      return 1;
    }
  }
  int ret_val = 1;
  while (num != 0){
    if (arr[num % 10]) {
      ret_val = 0;
      break;
    }
    num /= 10;
  }
  return ret_val;
}

int main(){
  int arr[10] = {0, };
  int target = 0;
  int ans = 0;
  int up = 0, down = 0;
  int upper_bound = 0;
  int lower_bound = 0;
  int len_broken = 0;
  int num = 0;

  scanf("%d", &target);
  up = target;
  down = target;
  upper_bound = MAX(100, 2 * target);
  scanf("%d", &len_broken);

  for (int i = 0; i < len_broken; i++){
    int tmp = 0;
    scanf("%d", &tmp);
    arr[tmp] = 1;
  }

  if (len_broken == 10){
    printf("%d\n", ABS(target - 100));
  }

  else{
    int seq = 1;

    while (1) {

      if (seq){
        if (down >= lower_bound){
          if (is_available(arr, down)){
            num = down;
            break;
          }
          else{
            down -= 1;
          }
        }
      }

      else{
        if (up <= upper_bound){
          if (is_available(arr, up)){
            num = up;
            break;
          }
          else{
            up += 1;
            ans += 1;
          }
        }
      }
      seq ^= 1;
    }

    printf("%d\n", MIN(ans + MIN(ABS(num - 100), len(num)) , ABS(target - 100)));
  }
}
