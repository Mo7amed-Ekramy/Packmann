import heapq

grid = [
    ['P', 0,  0,  0,  0,  0,  0,  0],
    [ 0,  1,  1,  0,  1, 'G',  1,  0],
    [ 0,  1,  0,  0,  0,  0,  1,  0],
    [ 0,  1,  0,  1,  1,  0,  1,  0],
    [ 0,  0,  0,  1, 'G', 0,  0,  0],
    [ 1,  1,  0,  1,  1,  1,  1,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  1,  1,  1,  1,  1,  0, 'F']
]

weights = {
    (1, 0): 15,
    (2, 0): 15,
    (3, 0): 15,
    (4, 0): 15,
    (4, 1): 15,

    (2, 4): 20,
    (2, 5): 20,
    (3, 5): 25,
    (4, 5): 25,

    (0, 3): 2,
    (0, 4): 2,
    (0, 5): 3,
    (2, 7): 2,
    (3, 7): 2,
    (4, 7): 4
}


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'P':
                return (i,j)


def get_neighbors(row, col, grid):
                # Down   Right    Left     UP
    directions = [(1,0),  (0,-1), (0,1), (-1,0)]
    neighbors = []
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            if grid[new_row][new_col] != 1:
                if grid[new_row][new_col] != 'G':
                    neighbors.append((new_row,new_col))
    return neighbors

def BFS(vertex):
    visited = set()
    visited.add(vertex)
    queue = [vertex]
    parent = {}
    goal = None
    
    while queue:
        current_vertex = queue.pop(0)
        
        row, col = current_vertex
        if grid[row][col] == 'F':
            goal = current_vertex
            break
        
        for neighbor in get_neighbors(current_vertex[0],current_vertex[1],grid):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = current_vertex

    if goal is None:
        print("No path found")
        return
    path = []
    current_vertex = goal

    while current_vertex in parent:
        path.append(current_vertex)
        current_vertex = parent[current_vertex]
    path.append(vertex)
    path.reverse()

    print("Path:", path)
    print("Steps:", len(path)-1)
    return path

def DFS(vertex):
    visited = set()
    visited.add(vertex)
    stack = [vertex]
    parent = {}
    goal = None
    
    while stack:
        current_vertex = stack.pop()
        
        row, col = current_vertex
        if grid[row][col] == 'F':
            goal = current_vertex
            break
        
        for neighbor in get_neighbors(current_vertex[0],current_vertex[1],grid):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                parent[neighbor] = current_vertex

    if goal is None:
        print("No path found")
        return
    path = []
    current_vertex = goal

    while current_vertex in parent:
        path.append(current_vertex)
        current_vertex = parent[current_vertex]
    path.append(vertex)
    path.reverse()

    print("Path:", path)
    print("Steps:", len(path)-1)
    return path


def Dijkstra(vertex):
    pq = [] #=> Min-Heap
    heapq.heappush(pq, (0, vertex))  # (cost, node)

    distance = {vertex: 0}
    parent = {}
    goal = None

    while pq:
        cost, current_vertex = heapq.heappop(pq)

        row, col = current_vertex

        # Goal Check
        if grid[row][col] == 'F':
            goal = current_vertex
            break

        for neighbor in get_neighbors(row, col, grid):
            if neighbor in weights:
                new_cost = cost + weights[neighbor]
            else:
                new_cost = cost +1
            
            if neighbor not in distance or new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                parent[neighbor] = current_vertex
                heapq.heappush(pq, (new_cost, neighbor))

    if goal is None:
        print("No path found")
        return

    path = []
    current_vertex = goal

    while current_vertex in parent:
        path.append(current_vertex)
        current_vertex = parent[current_vertex]

    path.append(vertex)
    path.reverse()

    print("Path:", path)
    print("Cost:", distance[goal])

    return path

start = find_start(grid)

print("=== BFS ===")
BFS(start)

print("\n=== DFS ===")
DFS(start)

print("\n=== Dijkstra ===")
Dijkstra(start)
