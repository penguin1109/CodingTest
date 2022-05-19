"""
13460. 구슬 탈출 2
빨간 구슬을 구멍을 통해 빼내는 것이 목표이고 파란 구슬은 구멍에 들어가면 안된다.
왼/오/위/아래로 기울여서 구슬을 움직일 수 있고 동시에 구멍에 빠져도 실패이다.
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하여
'.' : 빈 칸
'#' : 벽
'0' : 구멍
'R' : 빨간 구슬
'B' : 파란 구슬
10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 세로, 가로
board = []
red, blue = (0,0),(0,0)
## (1) 빨간 구슬과 파란 구슬과 구멍의 위치를 저장하고 문자 이동 판을 완성한다.
hole = (0,0)
for n in range(N):
    temp = []
    row = input().strip()
    for m in range(M):
        if row[m] == 'R':
            red = (n,m)
        elif row[m] == 'B':
            blue = (n,m)
        elif row[m] == 'O':
            hole = (n,m)
        temp.append(row[m])
    board.append(temp)

## (2) 한 번 기울일 때 빨간 구슬과 파란 구슬의 움직임을 모두 고려해야 한다.
dx, dy = [-1,1,0,0], [0,0,1,-1]
# 가로와 세로의 길이를 벗어나지 말아야 한다. (while문에서 조건으로 주어져야 함)
answer = 1000000
from collections import deque
q = deque()
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
q.append((red[0], red[1], blue[0], blue[1], 1))
visited[red[0]][red[1]][blue[0]][blue[1]] = True

def move(x,y,dir):
    """
    특정 지정된 dir이라는 방향으로 벽이나 구멍에 도달하기 전까지 이동한다.
    즉, 구멍에 도달하면 return
    """
    count = 0
    while(board[x + dx[dir]][y + dy[dir]] != '#' and board[x][y] != 'O'):
        x,y = x + dx[dir], y + dy[dir]
        count += 1
    return x, y, count

def bfs():
    while q:
        a,b,c,d,cnt = q.popleft()
        if (cnt > 10):break
        for i in range(4):
            rx,ry,rcnt = move(a,b,i)
            bx,by,bcnt = move(c,d,i)
            if board[bx][by] != 'O': ## 파란색이 구멍에 들어간게 아니라면 정답이 됨
                return cnt
            if (rx == bx and ry == by): ## 빨간 구슬과 파란 구슬이 같으면
                if (rcnt > bcnt): ## 빨간색이 더 많이 이동했으면
                    rx -= dx[i]
                    ry -= dy[i]
                else: ## 파란색이 더 많이 이동했으면
                    bx -= dx[i]
                    by -= dy[i]
            if not visited[rx][ry][bx][by]: ## 아직 방문하지 않은 경우에만 탐색을 한다.
                visited[rx][ry][bx][by] = True
                q.append((rx,ry,bx,by,cnt + 1))
    return -1
print(bfs())

"""
bfs, 즉 breadth first search는 너비 우선 탐색인데, 그래프 기반 탐색 알고리즘에서 중요한 것은
이미 방문한 곳을 다시 방문하지 않음으로서 시간 계산을 줄여주는 것이다.
먼저 특정 높이에서 방문할 수 있는 곳을 모두 이동한다.
"""
