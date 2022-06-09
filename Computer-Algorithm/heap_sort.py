n = 9
heap = [7,6,5,8,34,5,9,1,6]

def swap(arr, a,b): ## 배열에서 a번째 인덱스와 b번째 인덱스의 위치 변경
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr

for i in range(1, n):
    ## 전체 트리 구조를 최대 힙 구조로 바꾸어 준다.
    c = i
    while True:
        root = (c-1)//2
        if (heap[root] < heap[c]): ## 부모 노드가 더 작으면 최대 힙이 아니기 때문에
            heap = swap(heap, root, c)
        c = root
        if (c != 0):
            continue
        else:
            break
## 크기를 줄여가면서 반복적으로 힙을 구성한다.
for i in range(n-1, -1, -1): ## 힙의 크기
    heap = swap(heap, i, 0) ## 0번째 인덱스의 값과 i번째의 값 변경
    root = 0;c = 1;
    ## 가장 큰 값을 맨 뒤로 보내는 과정이다.
    while True:
        c = 2 * root + 1 ## 왼쪽 서브 트리의 루트 노드
        if c < i-1:
            if (heap[c] < heap[c+1]):c += 1 ## 더 큰 값을 갖는 노드로 변경
        if c < i:
            if (heap[root] < heap[c]): ## 부모 < 노드로 조건위배하면 swap
                heap = swap(heap, root, c)
        root = c
        if (c < i): ## 범위 벗어나지 않으면 이어서 반복
            continue
        else:
            break
    print(heap)
print(heap)