"""
풀 수 있는 문제 : P 문제 / NP 완전 문제 (주어진 시간에서 근삿값으로 해를 구할 수 밖에 없음)
NP이론
NP 문제 집합 : P 문제 집합과 NP 문제 집합을 둘 다 포함하는 문제의 집합을 의미한다.
NP 알고리즘
1. 주어진 입력에 대해서 하나의 해를 추측한다.
2. 그 추측한 해에 대해서 '다항식 시간 안에 확인' 한다.

NP-완전 문제를 해결하게 위해서는 원래 기존의 문제를 'yes/no'가 답이 되는 문제로 변형하여아한다. 이러한 유형의 문제를 '결정 문제'라고 한다.
MST를 구하기 위해서는 크루스칼 알고리즘이나 프림 알고리즘을 사용한다.
"""
def VertexCover(adj):
    V = len(adj)
    visited = [False] * V
    c = [] ## 정점 커버 집합
    for u in range(V):
        if visited[u] == False:
            for v in range(V):
                if adj[u][v] != 0 and visited[v] == False:
                    c.append(v);c.append(u); ## 극대 매칭 하는 과정
                    visited[v] = True;visited[u] = True; ## 이제 u, v와 인접한 간선은 방문할 필요가 없게 됨
                    break
    return c

g = [
    [0,1,0,0,0,0],[1,0,1,1,1,0],[0,1,0,0,1,1], [0,1,1,0,0,1],[0,0,1,0,1,0]
]
print(VertexCover(g)) ## 근사해를 구할 수 있게 된다.


"""
결국 찾고자 하는 근사해는 c의 정점의 개수이고, 이는 극대 매칭의 간선 수의 2배이다.
극대 매칭의 각 간선의 양쪽 끝점들의 집합을 정점 커버의 근사해로서 반환하므로 근사해의 값은 극대 매칭의 간선의 수의 2배이다.
근사 비율 = (극대 매칭의 각 간선의 양 끝점들의 수) / (극대 매칭의 간선의 수)
"""
path = []
tree = [[1,3,4],[0,2],[1,5],[0],[0],[2]] ## 최적의 MST를 찾은 상황이다.

visited = [False for _ in range(len(tree)+1)]
def dfs(v):
    visited[v] = True
    path.append(v)
    for w in tree[v]:
        if visited[w] == False:
            dfs(w)
            path.append(v) ## 백트래킹해서 되돌아와야 함


dfs(0)
print(path)

best = []
for p in path:
    if p not in best:
        best.append(p)
best.append(0) ## 다시 출발점으로 돌아와야 한다.
print(best)

"""
- 통 채우기 문제 : 통의 용량이 C일 때 n개의 물건을 가장 적은 수의 통에 채우는 문제 
-> 그리디 아이디어를 사용해서 "무엇에 욕심을 낼 것인가"에 따라 4종류로 분류 한다. 각 방법으로 새 물건을 기존의 통에 넣을 수 없다면 새로운 통에 새 물건을 담는다.
1. 최초 적함 : 첫 번째 통부터 차례로 살펴보면서 가장 먼저 여유가 있는 통에 새 물건을 넣는다.
2. 다음 적합 : "직전에" 물건을 넣은 통에 여유가 있으면 새 물건을 넣는다.
3. 최선 적합 : 기존의 통 중에서 새 물건이 들어가면 남는 부분이 가장 작은 통에 새 물건을 넣는다.
4. 최악 적합 : 기존의 통 중에서 새 물건이 들어가면 남는 부분이 가장 큰 통에 새 물건을 넣는다.
"""

N = 8
bin_size = 10 ## 통의 용량 C
item = [7,5,6,4,2,3,7,5] ## N개의 물건
bins = [[] for i in range(N)] ## 각각의 통에 어떤 물건이 들어가는지 (최대 사용하게 될 통의 수는 전체 물건의 개수인 N을 넘지 않을 것이다.)
remnant = [bin_size for _ in range(N)] ## 각 통에 남아있는 용량
bin_cnt = 1
## 아래 방법은 최초 적합 알고리즘을 사용하는 방법이다. 따라서 모든 통을 차례로 살피면서 가장 "먼저" 물건을 넣을 여유가 있는 통에 새 물건을 넣는다.
for i in range(N):
    j = 0;packed = False;
    while j < bin_cnt:
        if item[i] <= remnant[j]:
            bins[j].append([i, item[i]])
            remnant[j] -= item[i]
            packed = True
            break
        j += 1
    if not packed:
        bins[j].append([i, item[i]])
        remnant[j] -= item[i]
        bin_cnt += 1
print(bins)
print(bin_cnt)