print('EJEMPLO BASICO PRIMERO EN PROFUNDIDAD')
graph={'A': set(['B','C']),
       'B': set(['A','D','E']),
       'C': set(['A','F']),
       'D': set(['B']),
       'E': set(['B','F']),
       'F': set(['C','E'])}
def dfs(graph, inicio):
    visited, stack = set(), [inicio]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited
print(dfs(graph,'B'))
