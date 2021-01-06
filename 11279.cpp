#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <stdbool.h>
#include <string>

using namespace std;

typedef struct _queue* queue;
typedef struct _queue{
  int len;
  int capacity;
  int* arr;
}_queue;

queue make_queue(int capacity);
int is_min(int index);
void insert(queue q, int num);
void push_down(queue q, int index);
//void push_up(queue q, int index);
void push_down_min(queue q, int index);
void push_down_max(queue q, int index);
void push_up_min(queue q, int index, int num);
void push_up_max(queue q, int index, int num);
int get_child(queue q, int index);
int remove_max(queue q);
int remove_min(queue q);
void delete_queue(queue q);
void swap(int* x, int* y);

int main(){
  int case_num = 0;
  scanf("%d", &case_num);

  queue q = make_queue(case_num);
  for (int i = 0; i < case_num; i++){
    int num = 0;
    scanf("%d", &num);

    if (num > 0){
      insert(q, num);
    }
    else {
      num = remove_max(q);
      if (num < 0){
        printf("0\n");
      }
      else{
        printf("%d\n", num);
      }
    }
  }
}

queue make_queue(int capacity){
  queue q = (queue)malloc(sizeof(_queue));
  q->arr = (int*)malloc(sizeof(int) * (capacity + 1));
  q->len = 0;
  q->capacity = capacity;
  return q;
}

int is_min(int index){
  int count = 0;
  while (index){ count++;
    index /= 2;
  }
  return (count % 2 == 1) ? 1 : 0;
}

void insert(queue q, int num){
  if (q->len == q->capacity){
    printf("Queue is already full\n");
    return;
  }
  int index = ++(q->len);
  q->arr[index] = num;

  if (index == 1){
    return;
  }

  int parent = index / 2; 
  int min_level = is_min(parent);

  if (min_level){
    if (q->arr[index] < q->arr[parent]){
      q->arr[index] = q->arr[parent]; 
      push_up_min(q, parent, num);
    }
    else{
      push_up_max(q, index, num);
    }
  }
  else{
    if (q->arr[index] > q->arr[parent]){
      q->arr[index] = q->arr[parent];
      push_up_max(q, parent, num);
    }
    else{
      push_up_min(q, index, num);
    }
  }
}

int remove_max(queue q){
  if (q->len == 0){
    return -1;
  }
  else if (q->len == 1){
    return q->arr[(q->len)--];
  }
  else{
    int child = 2;
    if (q->len >= 3 && q->arr[3] > q->arr[child]){
      child = 3;
    }
    int ret_val = q->arr[child];
    q->arr[child] = q->arr[(q->len)--];
    push_down(q, child);
    return ret_val;
  }
}

int remove_min(queue q){
  if (q->len == 0){
    return -1;
  }
  else{
    int ret_val = q->arr[1];
    q->arr[1] = q->arr[(q->len)--];
    push_down(q, 1);
    return ret_val;
  }
}

void push_down(queue q, int index){
  if (is_min(index)){
    push_down_min(q, index);
  } 
  else{
    push_down_max(q, index);
  }
}

int get_child(queue q, int index){
  int min_level = is_min(index);
  int child[6] = {2 * index, 2 * index + 1, 4 * index, 4 * index + 1, 4 * index + 2, 4 * index + 3};
  int ret_val = child[0];
  if (min_level){
    int min = q->arr[child[0]];
    for (int i = 1; i < 6; i++){
      if (child[i] > q->len){
        break;
      } 
      else if (q->arr[child[i]] < min){
        ret_val = child[i];
        min = q->arr[child[i]];
      }
    }
  }
  else{
    int max = q->arr[child[0]];
    for (int i = 1; i < 6; i++){
      if (child[i] > q->len){
        break;
      } 
      else if (q->arr[child[i]] > max){
        ret_val = child[i];
        max = q->arr[child[i]];
      }
    }
  }
  return ret_val;
}

void push_down_min(queue q, int index){
  if (2 * index <= q->len){
    int child = get_child(q, index);
    if (child >= 4 * index){
      if (q->arr[child] < q->arr[index]){
        swap(&q->arr[index], &q->arr[child]);
        if (q->arr[child] > q->arr[child / 2]){
          swap(&q->arr[child], &q->arr[child / 2]);
        }
        push_down_min(q, child);
      }
    }
    else if (q->arr[child] < q->arr[index]){
      swap(&q->arr[index], &q->arr[child]);
    }
  }
}

void push_down_max(queue q, int index){
  if (2 * index <= q->len){
    int child = get_child(q, index);
    if (child >= 4 * index){
      if (q->arr[child] > q->arr[index]){
        swap(&q->arr[index], &q->arr[child]);
        if (q->arr[child] < q->arr[child / 2]){
          swap(&q->arr[child], &q->arr[child / 2]);
        }
        push_down_max(q, child);
      }
    }
    else if (q->arr[child] > q->arr[index]){
      swap(&q->arr[index], &q->arr[child]);
    }
  }
}

void push_up_max(queue q, int index, int num){
  int grandparent = index / 4;

  while (grandparent){
    if (q->arr[grandparent] < num){
      q->arr[index] = q->arr[grandparent];
      index = grandparent;
      grandparent /= 4;
    }
    else{
      break;
    }
  }
  q->arr[index] = num;
}

void push_up_min(queue q, int index, int num){
  int grandparent = index / 4;

  while (grandparent){
    if (q->arr[grandparent] > num){
      q->arr[index] = q->arr[grandparent];
      index = grandparent;
      grandparent /= 4;
    }
    else{
      break;
    }
  }
  q->arr[index] = num;
}
void delete_queue(queue q){
  free(q->arr);
  free(q);
}

void swap(int* x, int* y){
  int tmp = *x;
  *x = *y;
  *y = tmp;
}

