from collections import deque, defaultdict

def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    stack = deque([node for node in graph if in_degree[node] == 0])
    output = []

    while stack:
        u = stack.pop()
        output.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                stack.append(v)

    if len(output) < len(graph):
        raise ValueError("Graph has a cycle; topological ordering is impossible.")

    return output


