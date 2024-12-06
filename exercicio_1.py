import math
from collections import deque

# Representação do grafo
graph = {
    'A': {'B': 3, 'C': 4},
    'B': {'D': 4},
    'C': {'D': 3, 'E': 2},
    'D': {'F': 5},
    'E': {'F': 2},
    'F': {'G': 3},
    'G': {}
}

# Coordenadas dos nós para heurística
coordinates = {
    'A': (0, 0),
    'B': (2, 2),
    'C': (4, 0),
    'D': (6, 2),
    'E': (6, -2),
    'F': (8, 0),
    'G': (10, 0)
}

def euclidean_distance(node1, node2):
    """Calcula a distância euclidiana entre dois nós."""
    x1, y1 = coordinates[node1]
    x2, y2 = coordinates[node2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# DFS
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in path:
                if neighbor == goal:
                    return path + [neighbor]
                stack.append((neighbor, path + [neighbor]))
    return None

# BFS
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (node, path) = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in path:
                if neighbor == goal:
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
    return None

# A* Search
def a_star(graph, start, goal):
    open_set = [(0, start, [start])]  # (f_score, node, path)
    closed_set = set()
    g_scores = {start: 0}

    while open_set:
        open_set.sort()  # Ordenar pela menor f_score
        _, current, path = open_set.pop(0)

        if current == goal:
            return path

        closed_set.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor in closed_set:
                continue

            tentative_g_score = g_scores[current] + cost
            f_score = tentative_g_score + euclidean_distance(neighbor, goal)

            if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                open_set.append((f_score, neighbor, path + [neighbor]))

    return None

# Função principal
def main():
    start, goal = 'A', 'G'

    # Executar os algoritmos
    dfs_path = dfs(graph, start, goal)
    bfs_path = bfs(graph, start, goal)
    a_star_path = a_star(graph, start, goal)

    # Cálculo de custos
    def calculate_cost(path):
        return sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1)) if path else float('inf')

    dfs_cost = calculate_cost(dfs_path)
    bfs_cost = calculate_cost(bfs_path)
    a_star_cost = calculate_cost(a_star_path)

    # Mostrar resultados
    print("DFS:")
    print(f"  Caminho: {dfs_path}")
    print(f"  Custo: {dfs_cost}\n")

    print("BFS:")
    print(f"  Caminho: {bfs_path}")
    print(f"  Custo: {bfs_cost}\n")

    print("A*:")
    print(f"  Caminho: {a_star_path}")
    print(f"  Custo: {a_star_cost}\n")

# Executar
if __name__ == "__main__":
    main()
