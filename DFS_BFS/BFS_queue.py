graph = {  #방향그래프를 인접리스트로 구현
    1:[2,3,4], # key값은 출발 노드를 의미 value 값은 도착할 수 있는 노드를 의미
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3],
}

def BFS(G,start_v):
    visited = [start_v]
    queue = [start_v]
    
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
                
    return visited     

print(BFS(graph,1))