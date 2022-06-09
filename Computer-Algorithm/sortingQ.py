def partition2(A):
    left = 0;right = len(A)-1
    temp = 0
    while (left <= right):
        while (A[left] == 0):left +=1
        while (A[right] == 1):right-=1
        if (left < right): ## 이 때 0과 1을 SWAP하는 과정을 거친다.
            temp = A[left]
            A[left] = A[right]
            A[right] = temp
    return A

def swap(A, i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return A

def partition3(A):
    left = 0;right = len(A)-1;i = 0;
    temp = 0
    while (i<=right):
        if (A[i] == 0):
            A = swap(A, i, left) ## 0이면 왼쪽 끝과 SWAP
            i += 1;left += 1;
        elif (A[i] == 2):
            A = swap(A, i, right) ## 2이면 오른쪽 끝과 SWAP
            right -= 1;
        elif (A[i] == 1): ## 1이면 가운데 값이니까 SWAP를 할 필요가 없이 오른쪽으로 포인터를 이동하기만 한다.
            i += 1
    return A

def range_partition(A, lower, higher):
    ## 범위가 주어질때 범위 (1~lower-1) / (lower ~ higher) / (higher ~ ) 이렇게 3파트로 정렬이 되도록 한다.
    ## 단, 각각의 3파트 내에서는 정렬이 되지 않는다.
    ## lower보다 작은 수는 왼쪽에, higher보다 큰 수는 모두 오른쪽에 배치되도록 한다.
    left = 0;right = len(A)-1;i = 0;
    while (i <= right):
        if (A[i] < lower):
            A = swap(A, i, left)
            i += 1;left += 1;
        elif (A[i] > higher):
            A = swap(A, i, right)
            right -= 1
        else:
            i += 1

    return A

def sep_even_odd(A):
    ## 왼편에는 짝수가 오도록, 오른편에는 홀수가 오도록 배열을 바꾼다.
    left = 0;right = len(A)-1;
    while (left < right):
        if (A[left] % 2 == 0): ## 왼쪽에 짝수이면 포인터 이동
            left += 1
        elif (A[right] % 2 == 1): ## 오른쪽에 홀수이면 포인터 이동
            right -= 1
        else:
            A = swap(A, left, right) ## 왼쪽이 홀, 오른쪽이 짝이면 SWAP
            left += 1;right -= 1;
    return A

def partition(A, left, right, pivot):
    low = left-1;high = right + 1
    """
    do-while문을 파이썬으로 구현하면 아래와 같다.
    """
    while True:
        while True:
            low += 1
            ## 기준이 되는 문자와 동일하면
            if (A[low] == pivot):continue ## while문이 유지되기 위해서 만족해야 하는 조건
            break
        while True:
            high -= 1
            if (A[high] != pivot):continue
            break
        if (low < high): ## A[low]는 pivot이 아니고 A[high]는 pivot이 맞다면 바꿔 주어야 한다.
            A = swap(A, low, high)
            continue
        break

    return low
def sepColor(A, left, right):
    q = partition(A, left, right, 'R') ## 왼쪽에는 R, 오른쪽에는 R이 아닌 것
    print(A)
    partition(A, q, right, 'G') ## R이 아닌 index부터 왼쪽에는 G, 오른쪽에는 G가 아닌 것
    return A

import random

if __name__ == "__main__":
    A = []
    while (len(A) < 15):
        n = random.randint(1,100) % 3 ## 배열을 'R', 'G', 'B'의 3개의 문자로 채워야 하기 때문에 나머지를 사용해서 선택한다.
        if (n == 0):A.append('R')
        elif (n == 1):A.append('G')
        else:A.append('B')

    A = list(A)
    print(A)
    # A = range_partition(A,7,11)
    A = sepColor(A, 0, len(A)-1)
    for i in range(len(A)):
        print(A[i], end = ' ')