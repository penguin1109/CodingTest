"""
MST (Minimum Spanning Tree)
최소 신장 트리 알고리즘은 가중치를 갖는 간선들중에서 모든 노드들을 연결하면서 최소의 가중치로 이동할 수 있도록 노드를 연결한,
사이클이 없는 Tree를 만드는 것이 목적이다.
그렇다면 다음과 같은 부분을 확인해야 할 것이다.
1. 현재 노드를 추가하면 사이클이 존재하는지
2. 현재 노드가 이미 방문한 적이 있는 노드인지
백준의 15481번을 풀면서 크루스칼 알고리즘과 프림 알고리즘을 복습해 볼 예정이다.
"""
import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().split()) ## N개의 정점, M개의 간선
edges = [];data = [];parent = [i for i in range(N+1)]
G = [[] for _ in range(N+1)] ## MST를 만들기 위한 토대가 되는 그래프를 생성한다.
mst = 0 # MST의 가중합
l_parent = [[[0,0] for _ in range(21)]for _ in range(N+1)]
visit = [False for _ in range(N+1)]
level = [0 for _ in range(N+1)]
"""
이 문제는 다음과 같이 해결이 가능하다.
1. 먼저 주어진 노드와 간선들로 MST를 구한다.
2. 그리고 반드시 포함되어야 하는 간선이 이미 있다면 MST값을 그대로 출력하고, 아니라면 다른 간선을 빼서 사이클이 생기지 않도록 한다.

새로운 간선을 추가함으로서 생기는 사이클의 나머지 간선중 최대 가중치 간선을 골라서 끊어주면 된다.
LCA로 표시해서 공통 조상까지 올라오고 내려오는 경로에서 sparse table을 사용해서 효율적으로 최대 
가중치를 갖는 간선을 골라 주어야 한다.
"""
def find(node):
    ## tree를 만들기 위해서 조상을 찾아주는 과정
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u,v):
    ## 두 노드를 union 해서 연결 시켜 준다.
    pu, pv = parent[u], parent[v]
    if (pu > pv):
        parent[pu] = pv
    else:parent[pv] = pu

def dfs(node, depth):
    visit[node] = 1
    level[node] = depth
    for next_node, weight in G[node]:
        if (visit[next_node] == True):
            continue
        l_parent[next_node][0] = [node, weight]
        dfs(next_node, depth+1)

def set_parent():
    dfs(1, 0)
    for l in range(1, 21):
        for node in range(1, N+1):
            next_n, next_w = l_parent[node][l-1] ## 2_i위의 단계의 부모 노드에 대한 정보를 별도의 테이블에 저장한다.
            l_parent[node][l] = [l_parent[next_n][l-1][0], max(next_w, l_parent[next_n][l-1][1])]

def lca(high, low):
    ret = 0
    ## 무조건 low가 더 깊도록 변경
    if level[high] > level[low]:
        high, low = low, high
    ## 높이를 동일하게 맞춰줌
    for l in range(20, -1, -1):
        if level[low] - level[high] >= (2**l):
            ret = max(ret, l_parent[low][l][1])
            low = l_parent[low][l][0]
    if high == low: ## 부모가 이미 같으면 return
        return ret
    for l in range(20, -1, -1):
        if (l_parent[low][l][0] != l_parent[high][l][0]):
            ## 거슬러 올라가면서 (공통 조상에 도달할 때까지) 계속 최대 값을 갖는 가중치를 찾는다.
            ret = max(ret, max(l_parent[low][l][1], l_parent[high][l][1]))
            low = l_parent[low][l][0]
            high = l_parent[high][l][0]
    return max(ret, l_parent[low][0][1], l_parent[high][0][1]) ## 같은 사이클을 이루는 간선 중 최대 가중치를 반환

for _ in range(M):
    u,v,w = map(int, input().split())
    data.append((u,v,w))
    heapq.heappush(edges, (w, u,v))
while edges:
    w,u,v = heapq.heappop(edges)
    if find(u) != find(v):
        union(u, v)
        G[u].append((v,w));G[v].append((u,w))
        mst += w

set_parent()
for u, v, w in data:
    cost = lca(u, v)
    print(mst + w - cost)

