#include <cstdio>
#include <vector>
#include <cstdlib>

using namespace std;

typedef struct _node* node;
typedef struct _node{
    int exist;
    char color;
    vector<node> connect;
} _node;

char get_color(node n){

  char ret_val = n->color;

  if (n->color == 'W'){

    n->color = 'B';
    for (int i = 0; i < n->connect.size(); i++){
      get_color(n->connect[i]);
    }
  }

  return ret_val;
}

int main(){
  
  int case_num = 0;
  scanf("%d", &case_num);

  for (int i = 0; i < case_num; i++){
    int w, h, k;
    scanf("%d %d %d", &w, &h, &k);

    node* n = new node[w * h];

    for (int j = 0; j < w * h; j++){
      n[j] = new _node;
      n[j]->exist = 0;
      n[j]->color = 'W';
    }

    for (int j = 0; j < k; j++){
      int x, y;
      scanf("%d %d", &x, &y);
      int pos = y * w + x;
      n[pos]->exist = 1; 
      if (pos - 1 >= 0 && (pos - 1) / w == pos / w && n[pos - 1]->exist == 1){
        n[pos]->connect.push_back(n[pos - 1]);
        n[pos - 1]->connect.push_back(n[pos]);
      }
      if (pos + 1 < w * h && (pos + 1) / w == pos / w && n[pos + 1]->exist == 1){
        n[pos]->connect.push_back(n[pos + 1]);
        n[pos + 1]->connect.push_back(n[pos]);
      }
      if (pos - w >= 0 && n[pos - w]->exist == 1){
        n[pos]->connect.push_back(n[pos - w]);
        n[pos - w]->connect.push_back(n[pos]);
      }
      if (pos + w < w * h && n[pos + w]->exist == 1){
        n[pos]->connect.push_back(n[pos + w]);
        n[pos + w]->connect.push_back(n[pos]);
      }
    }

    int ans = 0;
    for (int j = 0; j < w * h; j++){
      if (n[j]->exist == 1 && get_color(n[j]) == 'W'){
        ans += 1;
      }
    }

    printf("%d\n", ans);
    for (int j = 0; j < w * h; j++){
      delete n[j];
    }
    delete n;
  }
}
