#include <iostream>
#define MAX 100001

using namespace std;

int in_order[MAX], post_order[MAX], idx[MAX];

void pre_order(int in_begin, int in_end, int post_begin, int post_end){
  
  if (in_begin > in_end || post_begin > post_end){
    return;
  }

  int root = post_order[post_end];

  int index = idx[root];

  cout << root << " ";

  pre_order(in_begin, index - 1, post_begin, post_begin + (index - in_begin) - 1);
  pre_order(index + 1, in_end, post_begin + (index - in_begin), post_end - 1);
  
}

int main(){
  int N;
  cin >> N;

  for (int i = 0; i < N; i++){
    cin >> in_order[i];
  }
  for (int i = 0; i < N; i++){
    cin >> post_order[i];
  }
  for (int i = 0; i < N; i++){
    idx[in_order[i]] = i;
  }

  pre_order(0, N - 1, 0, N - 1);
  cout << "\n";
}

