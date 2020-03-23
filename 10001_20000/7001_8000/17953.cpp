#include <bits/stdc++.h>

using namespace std;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);  
  int day, kind;

  cin >> day >> kind;
  int** desert = new int*[10];

  for (int i = 0; i < kind; i++){
    desert[i] = new int[day];
  }

  for (int i = 0; i < kind; i++){
    for (int j = 0; j < day; j++){
      cin >> desert[i][j];
    }
  }

  int dp[10][2] = {0};


  for (int i = 0; i < kind; i++){
    dp[i][0] = desert[i][0];
  }

  int idx = 0;

  for (int i = 1; i < day; i++){
    for (int j = 0; j < kind; j++){
      for (int k = 0; k < kind; k++){
        int val = dp[k][idx] + (j == k ? desert[j][i] / 2 : desert[j][i]);
        if (val > dp[j][idx ^ 1]){
          dp[j][idx ^ 1] = val;
        }
      }
    }
    idx ^= 1;
  }

  int ans = -1;

  for (int i = 0; i < kind; i++){
    if (ans < dp[i][idx]){
      ans = dp[i][idx];
    }
  }

  cout << ans << endl;

}


