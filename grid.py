grid = [
    ['P', 0, 0, 1],
    [ 0 , 1, 0, 1],
    [ 1 , 0, 0, 1],
    [ 0 , 0, 1,'G'],
    ['F', 1, 0, 0]
]


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'P':
                return (i,j)


def get_neighbors(row, col, grid):
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    grid = grid
    neighbors = []
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < len(grid):
            if 0 <= new_col < len(grid[0]):
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

BFS(find_start(grid))