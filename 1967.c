#include <stdio.h>
#include <stdlib.h>

int max_val = -1;

typedef struct _node* node;
typedef struct _node {
    int weight;
    /*int num;*/
    int len;
    int capacity;
    node* child;
} _node;

int get_weight(node n);

int main(){
    
    int input_len = 0;
    scanf("%d", &input_len);
    
    node* arr = (node*)malloc(sizeof(node) * (input_len + 1));

    for (int i = 0; i < input_len; i++){
       arr[i + 1] = (node)malloc(sizeof(_node));  
       arr[i + 1]->weight = 0;
       arr[i + 1]->child = (node*)calloc(10, sizeof(node));
       arr[i + 1]->capacity = 10;
       /*arr[i + 1]->num = i + 1;*/
    }

    for (int i = 0; i < input_len - 1; i++){
        int from, to, weight;
        scanf("%d %d %d", &from, &to, &weight);
        arr[to]->weight = weight;
        if (arr[from]->capacity == arr[from]->len){
            arr[from]->capacity *= 2;
            arr[from]->child = (node*)realloc(arr[from]->child, arr[from]->capacity * sizeof(node));
        }
        arr[from]->child[arr[from]->len++] = arr[to];
    }

    /*
     *for (int i = 1; i < input_len + 1; i++){
     *    printf("num --> %d / weight --> %d\n", arr[i]->num, arr[i]->weight);
     *}
     */

    get_weight(arr[1]);

    printf("%d\n", max_val);
}

int get_weight(node n){
    if (n == NULL){
        return 0;
    }

    int* w = (int*)calloc(n->len, sizeof(int));

    for (int i = 0; i < n->len; i++){
      w[i] = get_weight(n->child[i]);
    }

    int max2 = 0;
    int max1 = 0;

    for (int i = 0; i < n->len; i++){
      if (max1 < w[i]){
        max2 = max1;
        max1 = w[i];
      }
      else if (max2 < w[i]){
          max2 = w[i];
      }
    }

    if (max_val < max1 + max2){
      max_val = max1 + max2;
      /*
       *printf("num --> %d\tweight --> %d\n", n->num, max_val);
       *for (int i = 0; i < n->len; i++){
       *    printf("%d    ", w[i]);
       *}
       *    printf("\ntmp1 --> %d\ttmp2 --> %d", tmp1, tmp2);
       *    printf("\nmax1 --> %d\tmax2 --> %d\n", max1, max2);
       *printf("\n================\n");
       */
    }

    n->weight += max1;

    return n->weight;
}


