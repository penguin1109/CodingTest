def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

## 1-(1) 선택 정렬 : 순서대로 정렬후 i번째 위치에 올 원소를 선택해서 찾아줌
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        ## i번째 위치에 올 원소를 선택해서 찾아 주어야 한다.
        minNum = 10**8;minIdx = i;
        for j in range(n-1, i, -1): ## 뒤에서부터 비교해서 와야 한다.
            if minNum > arr[j]:
                minIdx = j;minNum = arr[j];
        arr = swap(arr, i, minIdx)
    return arr
## 1-(2) 버블 정렬 : 당장 바로 옆과 반복해서 비교
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i):
            if (arr[i] < arr[j]):
                arr = swap(arr, i, j)
    return arr
## 2-(1) 삽입 정렬 : 배열의 앞부분을 정렬 된 부분, 뒷부분을 정렬되지 않은 부분으로 놓고
# 정렬 안된 부분의 가장 왼쪽 원소를 정렬된 부분의 알맞은 위치에 넣어준다. (필요할 때만 위치를 바꾸기 때문에 이득)
def insertion_sort(arr):
    # 거의 정렬된 산태에서 제일 효율적이다.
    # O(N^2)로 시간 복잡도는 버블, 선택과 같지만 (while문 2번) 실제로는 연산량이 제일 적다.
    n = len(arr)
    for idx in range(n-2):
        j = idx
        while (j >= 0 and arr[j] > arr[j+1]):
            arr = swap(arr, j, j+1)
            j -= 1
    return arr
## 2-(2) 쉘 정렬 : 삽입 정렬을 사용해서 배열의 뒷부분의 작은 숫자를 앞부분으로 빠르게 이동 시키고
# 동시에 앞부분의 큰 숫자는 뒷부분로 빠르게 이동 시킨다.
def shell_sort(arr, gap):
    ## gap를 제일 큰 간격부터 1까지 그룹으로 나누너 비교한다
    for g in range(gap, 0, -1): ## 마지막에는 반드시 간격 1로 놓고 비교
        for i in range(g, len(arr)):
            curr = arr[i]
            j = i
            while (j >= g and arr[j-g] > curr):
                ## 큰걸 앞으로 보냄
                arr[j] = arr[j-g];j = j-g;
            arr[j] = curr
    return arr

## 3. 힙 정렬 : 정렬할 입력으로 최대 힙(부모 노드 > 자식 노드)을 만든다.
class Node:
    def __init__(self, key=-1, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def insert_node(root, key):
    if root == None:
        return Node(key)
    else:
        if (key < root.key): ## 넣어주려는 노드보다 큰 값이라면 왼쪽 서브 트리에 추가
            root.left = insert_node(root.left, key)
        elif (key > root.key): ## 넣어주려는 노드부다 작은 값이라면 오른쪽 서브 트리에 추가
            root.right = insert_node(root.right, key)
        else:
            return root
    return root

def heapify(arr):
    root = None
    for a in arr:
        root = insert_node(root, a)
    return root

def inorder(root):
    if (root == None):
        return
    inorder(root.left)
    print(root.key, end = ' ')
    inorder(root.right)

def heap_sort(arr):
    arr = heapify(arr)
    inorder(arr)

if __name__ == "__main__":
    import random
    arr = []
    for i in range(10):
        arr.append(random.randint(1, 100))
    print(arr)
    heap_sort(arr)
