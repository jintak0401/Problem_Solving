#include <string>
#include <iostream>

using namespace std;

int main(){
  string str, cmp;
  cin >> str >> cmp;
  char ans[1000001];
  int index = 0;

  for (int i = 0; i < str.size(); i++){
    ans[index++] = str[i];
    if (index >= cmp.size() && ans[index - 1] == cmp[cmp.size() - 1]){
      int pos = index - 2;
      int cmp_pos = cmp.size() - 2;
      for (; cmp_pos >= 0; pos--, cmp_pos--){
        if (ans[pos] != cmp[cmp_pos]){
          break;
        }
      }
      if (cmp_pos == -1){
        index -= cmp.size();
      }
    }
  }
  if (index == 0){
    printf("FRULA\n");
  }
  else{
    for (int i = 0; i < index; i++){
      printf("%c", ans[i]);
    }
    printf("\n");
  }
}

