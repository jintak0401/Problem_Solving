#include <iostream>
#include <algorithm>
#define MOD 1000000007l

using namespace std;

typedef long long ll;

int main(){

  cin.tie(NULL);
  ios::sync_with_stdio(false);

  int len = 0;
  ll ans = 0;
  int* arr = new int[300000];
  ll* power = new ll[300000];

  cin >> len;

  for (int i = 0; i < len; i++){
    cin >> arr[i];
    power[i] = (i == 0) ? 1 : power[i - 1] << 1;
    power[i] %= MOD;

  }

  sort(arr, arr + len);
  for (int i = 0; i < len; i++){
    ans += (arr[i] % MOD) * power[i] % MOD;
    ans -= (arr[i] % MOD) * power[len - i - 1] % MOD;
    ans = ((ans % MOD) + MOD) % MOD;
  }

  cout << ans << endl;
  
}

