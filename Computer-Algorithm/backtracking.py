import sys
## 백트래킹
"""
- 깊이 우선 탐색 (DFS)
- 상태 공간 트리를 루트에서부터 깊이 우선으로 탐색해 내려오다가 마지막 노드까지 가기 전에 방문한 어떤 노드가 해가 아니라고 판단 (=가지치기) 되면 이전 노드로 돌아오는 BACKTRACKING
- 최적화 / 결정 문제를 해결하는데 사용

** 배운 적용 부분들 **
1. 순열 구하기 (permutation)
2. 그래프 색칠하기 (그래프가 주어지고 인접한 노드들을 같은 색으로 칠할 수 없을 때 백트래킹 사용 가능)
3. 여왕 말 문제 (체스판에서 -> 막히면, 즉 퀸을 놓을 곳이 없으면 백트래킹해서 이전 단계의 다음 칸에 배치) -> 막히는 경우는 팔방으로 다른 퀸이 존재하는 경우이다.
"""
## NQueen 문제
"""
NxN인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하여라
알고리즘 : 백트래킹
-> 문제는 pypy3 으로 실행했을 때에만 시간 초과가 나지 않는다는 것이다.
"""
N = int(input()) # 체스판의 크기
ck = [[0]* N for _ in range(N)]

answer = 0
import math
def check_valid(x, y):
    ## 가로 / 세로 방향 확인
    for i in range(x):
        if ck[i][y] == 1:
            return False
    ## 대각선 확인
    for i in range(x):
        for j in range(N):
            if ck[i][j] == 1 and (abs(i-x) == abs(j-y)):
                return False
    return True

def nqueen(i):
    global answer
    if i == N:
        answer += 1
        return
    for j in range(N):
        if ck_row[j] == -1:
            valid = True
            for m in range(i): ## 가로 열 인덱스
                if (abs(j-ck_side[m]) == abs(m-i)): ## 같은 대각선상에 존재하면
                    valid = False
                    continue
            if valid:
                ck_row[j] = 0;ck_side[i] = j; ## 이번 경우에 대해 배열 갱신
                nqueen(i+1) ## 재귀 호출 -> 재귀 함수 실행 후 return 하면
                ck_row[j] = -1;ck_side[i] = -1; ## 원상 복귀

for i in range(N):
    ck_row = [-1]*N;ck_side = [-1]*N;
    ck_row[i] = 0;ck_side[0] = i;
    nqueen(1)
print(answer)

class color:
    def __init__(self):
        self.g = [[0,1,0,1,1,1],
                  [1,0,1,1,0,1],
                  [0,1,0,1,0,0],
                  [1,1,1,0,1,0],
                  [1,0,0,1,0,1],
                  [1,1,0,0,1,0]] ## 색칠해야 하는 그래프
        self.n = len(self.g) ## 그래프에 있는 노드의 개수
        self.color = [-1 * self.n]
        self.K = 3 ## 사용하는 색깔의 종류의 수

    def valid_check(self, i):
        for j in range(self.n):
            if (self.g[i][j] == 1) and (self.color[j] == self.color[i]) and (self.color[i] != -1):
                return False
        return True
    def coloring(self, i):
        if (i == self.n):
            print(self.color)
            return True
        for c in range(self.K):
            self.color[i] = c
            if (self.valid_check(i)): # 인접한 색과 겹치지 않는지 확인
                if self.coloring(i+1): # 재귀 호출했을 때도 가능하면
                    return True
        return False


class permutation:
    def __init__(self):
        self.result = []
        self.prev_elements = []

    def solution(self, elements):
        if (len(elements) == 0):
            self.result.append(self.prev_elements[:])
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e) ## 현재 사용할 원소 제거
            self.prev_elements.append(e)
            self.solution(next_elements) ## 재귀적으로 남은 숫자들을 한번씩 숫자 바꿔가면서 선택
            self.prev_elements.pop() ## 재귀 호출을 모두 했으니 이제는 pop
        return self.result

pem = permutation()
print(pem.solution([0,1,2]))