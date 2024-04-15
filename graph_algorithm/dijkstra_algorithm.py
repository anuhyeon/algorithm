###다익스트라 알고리즘 반복문으로 구현 --> 시간복잡도: O(n^2)

import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())

#그래프
graph = [[] for _ in range(n+1)]
#방문한 노드 체크
visited = [0]*(n+1)
#거리 저장 배열 (계속 최단 경로로 업데이트 시켜줌)
distance = [int(1e9)]*(n+1)

# 그래프 생성 (무방향 / 방향 잘 체크 할 것)
for _ in range(m): # 일단 무방향
    u,v,w = map(int,sys.stdin.readline().split()) # 출발노드,도착노드,가중치 입력 받기
    graph[u].append((v,w))
    graph[v].append((u,w))
print(graph)
def smallDistanceNode():
    min = int(1e9)
    idx = 0
    for i in range(1,n+1):
        if visited[i] == 0 and distance[i] < min:
            min = distance[i]
            idx = i
    return idx
    
def dijkstra(start_node):
    distance[start_node] = 0
    visited[start_node] = 1
    for next,w in graph[start_node]:
        distance[next] = w
    
    #start_node부터 start_node까지 거리는 0이므로 제외 --> n-1
    for _ in range(n-1): # start를 제외한 노드들을 우리가 돌아다니면서 최단경로를 파악해야하므로 (n-1) 만큼의 반복문을 돌려줘야함
        now = smallDistanceNode() #방문안한 노드중 가장 작은 노드 방문
        visited[now] = 1
        
        for next,w in graph[now]:
            #현재 노드에서 갈 수 있는 다른 노드 비용 계산
            cost = distance[now] + w
            # 기존보다 짧으면 갱신
            if cost < distance[next]:
                distance[next] = cost

dijkstra(1)

print(distance)

# 8 14
# 1 2 3
# 1 3 4
# 2 3 5
# 2 4 10
# 2 6 9
# 3 4 8
# 3 5 5
# 5 7 4
# 5 4 6
# 7 4 7
# 7 8 5
# 4 6 10
# 4 8 3
# 6 8 2