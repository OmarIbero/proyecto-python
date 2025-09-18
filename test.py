
knowledge = [
    ("A", "B", "L1", 4),
    ("B", "C", "L1", 6),
    ("C", "D", "L1", 5),
    ("B", "E", "L2", 10),
    ("E", "F", "L2", 3),
    ("F", "D", "L2", 8),
]


graph = {}
for a, b, line, time in knowledge:
    graph.setdefault(a, []).append((b, time, line))
    graph.setdefault(b, []).append((a, time, line))  


import heapq

def best_route(start, goal):
    pq = [(0, start, [])] 
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)


        path = path + [node]

        if node == goal:
            return cost, path 

        for neigh, t, line in graph.get(node, []):
            if neigh not in visited:
                heapq.heappush(pq, (cost + t, neigh, path))

    return None

# --- Ejemplo de uso ---
if __name__ == "__main__":
    inicio, fin = "A", "D"
    cost, path = best_route(inicio, fin)
    print(f"Mejor ruta de {inicio} a {fin}: {path}, con tiempo total {cost} minutos")
