import sys
from collections import deque

#graph = {0: [1, 2, 3], 1: [4], 2: [4, 5], 3: [], 4:[6], 5:[1], 6: []}

# 노드의 개수와 간서의 개수 입력
n,m = map(int,sys.stdin.readline().split()) # 노드의 개수와 간선의 개수 입력
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [[]for _ in range(n+1)]
answer = []
visited = [0]*(n+1)
for _ in range(m):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v) #  u -> v 방향그래프
    
                
def dfs_recurs(G,start,visited = []):
    visited.append(start)
    for w in G[start]:
        if w not in visited:
            dfs_recurs(G,w,visited)
    answer.append(start)

# def dfs_recurs(G, start, visited=None, answer=None):
#     if visited is None:
#         visited = []
#     if answer is None:
#         answer = []
#     visited.append(start)
#     for w in G[start]:
#         if w not in visited:
#             dfs_recurs(G, w, visited, answer)
#     answer.append(start)
#     return answer

# graph = {1: [5, 2], 2: [3], 3: [4], 4: [6], 5: [6], 6: [7]}
# visited = []
# answer = dfs_recurs(graph, 1)
# print([x for x in reversed(answer)])                

# def topology_sort_stack(G,start,visited):
#     ####dfs###
#     for i in range(1,len(G)):
#         if i not in visited:
#             dfs_recurs(G,i,visited)
#     print([x for x in reversed(answer)])
   
    
dfs_recurs(graph,1,visited)
print([x for x in reversed(answer)])
print(graph)
          
# 7 7
# 1 5
# 1 2
# 2 3
# 3 4
# 4 6
# 5 6
# 6 7
# [1, 5, 2, 3, 4, 6, 7]
# 1 2 3 4 5 6 7의 결과도 나올 수 있ㅇ므

# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
# [1, 5, 2, 6, 3, 4, 7]


class MyGraph:
    def __init__(self, N):
        self.vertexCnt = N
        self.edge_List = [[] for _ in range(N + 1)]
        self.visit = [False] * (self.vertexCnt + 1)  # 방문 표시
        self.finish = [False] * (self.vertexCnt + 1)  # 사이클 판단
        self.answer = []  # 결과를 담을 리스트
        self.cycle = False

    def insert_Edge(self, from_, to):
        self.edge_List[from_].append(to)

    def topological_Sort(self):
        # 방문하지 않은 정점을 DFS 수행
        for i in range(1, self.vertexCnt + 1):
            if self.cycle:
                print("그래프에 사이클 존재")
                return
            if not self.visit[i]:
                self.dfs(i)

        # 스택에 담긴 정점들을 출력
        print(" ".join(map(str, reversed(self.answer))))

    def dfs(self, v):
        self.visit[v] = True

        for nv in self.edge_List[v]:
            # 방문하지 않았으면 DFS 수행
            if not self.visit[nv]:
                self.dfs(nv)
            # 방문한 정점인데 finish 체크가 되지 않았으면 사이클이 존재한다는 의미
            elif not self.finish[nv]:
                self.cycle = True
                return

        # 더 이상 갈 곳이 없는 정점을 finish 체크 & 리스트에 넣어줌 (말단부터 상위로)
        self.finish[v] = True
        self.answer.append(v)


# # 테스트용 코드
# mg = MyGraph(7)
# mg.insert_Edge(1, 2)
# mg.insert_Edge(1, 3)
# mg.insert_Edge(1, 4)
# mg.insert_Edge(2, 5)
# mg.insert_Edge(2, 6)
# mg.insert_Edge(3, 7)
# mg.insert_Edge(3, 6)
# mg.insert_Edge(4, 3)
# mg.insert_Edge(6, 5)
# mg.topological_Sort()
