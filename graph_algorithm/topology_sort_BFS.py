import sys
from collections import deque

# 노드의 개수와 간서의 개수 입력
n,m = map(int,sys.stdin.readline().split()) # 노드의 개수와 간선의 개수 입력
# 모든 노드에 대한 진입차수는 일단 0으로 초기화함
indegree = [0] * (n+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [[]for _ in range(n+1)]

for _ in range(m):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v) #  u -> v 방향그래프
    indegree[v] += 1

# 위상 정렬 함수 BFS
def topology_sort(G):
    result = []
    queue = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        v = queue.popleft()
        result.append(v)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 뺴기
        for w in G[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)
                
    
    return result

print(topology_sort(graph))
    
             