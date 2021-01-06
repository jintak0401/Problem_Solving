#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<vector<int>> get_mat(std::vector<vector<int>>& mat, string a, string b){

  vector<vector<int>> dir(mat.size(), vector<int>(mat[0].size(), 0));
  for (int i = 1; i < mat.size(); i++){
    for (int j = 1; j < mat[i].size(); j++){
      if (a[i - 1] == b[j - 1]){
        mat[i][j] = mat[i - 1][j - 1] + 1;
      } 
      else if (mat[i][j - 1] < mat[i - 1][j]){
        mat[i][j] = mat[i - 1][j];
        dir[i][j] = 1;
      }
      else{
        mat[i][j] = mat[i][j - 1];
        dir[i][j] = -1;
      }
    }
  } 
  return dir;
}

string get_ans(std::vector<vector<int>> mat, string a, string b, vector<vector<int>> dir){
  string ans = "";
  int index = mat[mat.size() - 1][mat[0].size() - 1];
  int a_pos = a.size();
  int b_pos = b.size();

  while (index > 0){
    if (dir[a_pos][b_pos] == 0){
      ans = a[a_pos - 1] + ans;
      a_pos--;
      b_pos--;
      index--;
    }
    else if (dir[a_pos][b_pos] == 1){
      a_pos--;
    }
    else{
      b_pos--;
    }

  }
  return ans;
}

int main(){
  string a, b;
  cin >> a;
  cin >> b;
  vector<vector<int>> mat(a.size() + 1, vector<int>(b.size() + 1, 0));
  vector<vector<int>> dir = get_mat(mat, a, b);
  string ans = get_ans(mat, a, b, dir) ;
  int val = mat[mat.size() - 1][mat[0].size() - 1];
  cout << val << endl << ans << endl;
}

