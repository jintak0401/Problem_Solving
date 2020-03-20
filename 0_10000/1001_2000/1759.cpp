#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

char vowel[5] = {'a', 'e', 'i', 'o', 'u'};
int code_len = 0;

bool check_condition(std::string code){
  int count = 0;
  for (int i = 0; i < 5; i++){
    count += (code.find(vowel[i]) != -1);
  }

  if (count >= 1 && code.size() - count >= 2){
    return true;
  }

  else{
    return false;
  }
}

void get_ans(std::vector<char> letter, int index, string code){

  if (code.size() == code_len && check_condition(code)){
    cout << code << endl;
    return;
  }
  else if (code.size() < code_len){
    string origin = code;
    int remain_len = code_len - code.size();
    for (int i = index; i < letter.size() - remain_len + 1; i++){
      string tmp_code = origin + letter[i];
      get_ans(letter, i + 1, tmp_code);
    }
  }
}





int main(){
  int letter_len = 0;
  scanf("%d", &code_len);
  scanf("%d", &letter_len);

  std::vector<char> letter(letter_len);

  for (int i = 0; i < letter_len; i++)
  {
    getchar();
    scanf("%c", &letter[i]);

  }

  sort(letter.begin(), letter.end());


  get_ans(letter, 0, "");

}

