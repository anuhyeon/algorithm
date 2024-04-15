#재귀x 스택사용하여 구현
graph = {  #방향그래프를 인접리스트로 구현
    1:[2,3,4], # key값은 출발 노드를 의미 value 값은 도착할 수 있는 노드를 의미
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3],
}

def DFS(G,start_v): #G는 그래프: 딕셔너리로 구현 / v(vertex: 정점): 노드를 의미
    visited = []
    stack = [start_v]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for w in G[node]:
                stack.append(w)
    
    return visited

print(DFS(graph,1))
        