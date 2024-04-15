import sys
import heapq
n, m = map(int,sys.stdin.readline().split())

#그래프
graph = [[] for _ in range(n+1)]
#방문한 노드 체크
#visited = [0]*(n+1)
#거리 저장 배열 (계속 최단 경로로 업데이트 시켜줌)
distance = [int(1e9)]*(n+1)

# 그래프 생성 (무방향 / 방향 잘 체크 할 것)
for _ in range(m): # 일단 무방향
    u,v,w = map(int,sys.stdin.readline().split()) # 출발노드,도착노드,가중치 입력 받기
    graph[u].append((v,w))
    graph[v].append((u,w))
print(graph)

def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0
    while queue:
        #최단거리가 가장 짧은 노드에 대한 정보 추출
        dist, now = heapq.heappop(queue)
        #현재 처리된적 있는 노드라면
        if distance[now] < dist:
             continue
        for next,weight in graph[now]:
            cost = dist + weight
            #현재ㅐ 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(queue,(cost,next))


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