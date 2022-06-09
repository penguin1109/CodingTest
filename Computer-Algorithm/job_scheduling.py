"""
- 작업 스케줄링 문제
: n개의 작업의 수행 시간과 m개의 기계가 주어질 때 모든 작업이 가장 빨리 종료되도록 작업을 기계에 배정하는 문제이다.
-> 그리디 방법으로 작업을 배정하는, 즉 현재까지 배정된 작업에 대해 가장 빨리 끝나는 기계에 새 작업을 배정하는 방법을 사용할 수 있다.
"""
def job_scheduling(jobs, machine):
    schedule = [0 for _ in range(machine)] ## 각각의 기계의 마지막 종료 시간을 나타낸다.
    for i in range(len(jobs)): ## 작업 i를 어떤 기계에 배정할지 생각
        min = 0
        for j in range(1, machine):
            if (schedule[j] < schedule[min]): ## 모든 기계의 마지막 작업 종료 시간을 살펴 보아야 하므로 O(machine개수)만큼의 시간 복잡도를 필요로 한다.
                min = j ## 더 빨리 이전 작업이 끝나는 기계 선택
        schedule[min] += jobs[i]
    return max(schedule)

jobs = [5,2,4,3,4,7,9,2,4,1]
machine = 4
print(job_scheduling(jobs, machine))

"""
클러스터링 문제 : n개의 점을 k개의 그룹으로 나누고 각 그룹의 중심이 되는 k개의 점을 선택하는 문제이다.
- 단, 가장 큰 반경을 가진 그룹의 직경이 최소가 되도록 k개의 점을 선택하여야 한다.
"""
X = [[0,1,1],[1,9,8],[2,2,2],[3,7,2],[4,8,3],
     [5,3,4],[6,1,6],[7,1,9],[8,7,7],[9,3,8],
     [10,6,3],[11,8,6],[12,6,1],[13,3,2],[14,3,3],
     [15,7,3],[16,4,7],[17,8,8],[18,1,2],[19,10,10]]
groupN = 4
N = len(X)
C = []
D = [[] for _ in range(N)]
isCenter = [False for _ in range(N)]
import random,math
i = random.randint(0, N-1)
C.append(X[i]);isCenter[i] = True;centerCnt = 1; ## 첫번째 center은 임의로 지정해 준다.
## 결국 처음에 랜덤하게 설정되는 중심에 따라서 이후 중심들의 정확도가 달라지게 된다는 것이다.
## 따라서 실제로는 제일 나은 centroid를 찾기 위해서 알고리즘을 여러 차례 수행하여 얻은 결과중 best cluster을 사용하는 것이 맞다.
while centerCnt < groupN: ## 전체 군집의 개수보다 center의 개수가 적을 동안에 center을 찾는 과정을 반복한다.
    for i in range(N):
        if isCenter[i] == False: ## center이 아닌 경우
            D[i] = [-1, float('inf')]
            for j in range(centerCnt):
                dist = int(math.sqrt((C[j][1] - X[i][1])**2 + (C[j][2] - X[i][2]) ** 2)) ## center들과 현재 i번째 점 사이의 거리 계산
                if D[i][1] > dist:
                    D[i] = [j, dist] ## j : center 번호
    farthest = 0
    for i in range(N):
        if (not isCenter[i] and farthest < D[i][1]):
            farthest = D[i][1]
            nextCenter = i ## 기존 센터들과의 거리가 제일 먼 점이 다음 center이 된다.
    C.append(X[nextCenter])
    isCenter[nextCenter] = True
    centerCnt += 1
for i in range(groupN):
    print(f"Cluster  {i+1} : {C[i]}")
