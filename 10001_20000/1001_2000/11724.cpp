#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

typedef struct _node* node;
typedef struct _node {

    char color;
    vector<node> connect;

}_node;

char get_color(node n){

  char ret_val = n->color;

  if (ret_val == 'W'){
    n->color = 'G';

    for (int i = 0; i < n->connect.size(); i++){
      get_color(n->connect[i]);
    }

    n->color = 'B';
  }

  return ret_val;
}

int main(){
  int node_num, branch_num;

  scanf("%d %d", &node_num, &branch_num);

  node* n = new node[node_num + 1];

  for (int i = 1; i < node_num + 1; i++){
    n[i] = new _node;
    n[i]->color = 'W';
  }

  for (int i = 0; i < branch_num; i++){
    int a, b;
    scanf("%d %d", &a, &b);
    n[a]->connect.push_back(n[b]);
    n[b]->connect.push_back(n[a]);
  }

  int ans = 0;
  for (int i = 1; i < node_num + 1; i++){
    char get_ans = get_color(n[i]);
    if (get_ans == 'W'){
      ans += 1;
    }
  }
  printf("%d\n", ans);
}
