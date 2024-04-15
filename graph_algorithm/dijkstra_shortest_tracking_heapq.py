import sys
import heapq
n, m = map(int,sys.stdin.readline().split())

#그래프
graph = [[] for _ in range(n+1)]
#방문한 노드 체크
#visited = [0]*(n+1)
#[최단거리, 부모노드] 저장 테이블
distance = [[int(1e9),i]for i in range(1+n)]

# 그래프 생성 (무방향 / 방향 잘 체크 할 것)
for _ in range(m): # 일단 무방향
    u,v,w = map(int,sys.stdin.readline().split()) # 출발노드,도착노드,가중치 입력 받기
    graph[u].append((v,w))
    graph[v].append((u,w))
print(graph)

def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start][0] = 0
    while queue:
        #최단거리가 가장 짧은 노드에 대한 정보 추출
        dist, now = heapq.heappop(queue)
        #현재 처리된적 있는 노드라면
        # if distance[now] < dist:  # 지원도 상관 없나??? 상관 없는 거 같은디
        #     continue
        for next,weight in graph[now]:
            cost = dist + weight
            #현재ㅐ 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next][0]:
                distance[next][0] = cost # 최단거리 갱신
                distance[next][1] = now # 부모노드 저장
                heapq.heappush(queue,(cost,next))


dijkstra(1)
# print(distance)

# 결과 출력
for i in range(1,n+1):
    length,_= distance[i] # 최단 길이
    parent_node=i
    path=[]
    while parent_node!=1:        
        path.append(parent_node)    
        _,parent_node = distance[parent_node]
        distance[parent_node]
    path.append(1)
    print("%s번 노드 : %s (%s)" % (i,">".join(map(str,path[::-1])),length))


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