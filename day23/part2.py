"""
--- Part Two ---
As you reach the trailhead, you realize that the ground isn't as slippery as you expected; you'll have no problem climbing up the steep slopes.

Now, treat all slopes as if they were normal paths (.). You still want to make sure you have the most scenic hike possible, so continue to ensure that you never step onto the same tile twice. What is the longest hike you can take?

In the example above, this increases the longest hike to 154 steps:

#S#####################
#OOOOOOO#########OOO###
#######O#########O#O###
###OOOOO#.>OOO###O#O###
###O#####.#O#O###O#O###
###O>...#.#O#OOOOO#OOO#
###O###.#.#O#########O#
###OOO#.#.#OOOOOOO#OOO#
#####O#.#.#######O#O###
#OOOOO#.#.#OOOOOOO#OOO#
#O#####.#.#O#########O#
#O#OOO#...#OOO###...>O#
#O#O#O#######O###.###O#
#OOO#O>.#...>O>.#.###O#
#####O#.#.###O#.#.###O#
#OOOOO#...#OOO#.#.#OOO#
#O#########O###.#.#O###
#OOO###OOO#OOO#...#O###
###O###O#O###O#####O###
#OOO#OOO#O#OOO>.#.>O###
#O###O###O#O###.#.#O###
#OOOOO###OOO###...#OOO#
#####################O#
Find the longest hike you can take through the surprisingly dry hiking trails listed on your map. How many steps long is the longest hike?
"""

from collections import deque

def validate(matrix, row, col):
    return (
        0 <= row < len(matrix)
        and 0 <= col < len(matrix[0])
        and matrix[row][col] != "#"
    )

def find_neighbours(matrix, row, col):
    neighbours = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        if validate(matrix, new_row, new_col):
            neighbours.append((new_row, new_col))
    return neighbours


def find_intersections(matrix):
    intersections = []
    for i, row in enumerate(matrix):
        for j, tile in enumerate(row):
            if tile != "#" and len(find_neighbours(matrix, i, j)) > 2:
                intersections.append((i, j))
    return intersections


def bfs_search(matrix, start, intersections):
    distances = {}
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        (row, col), dist = queue.popleft()
        if (row, col) in intersections and (row, col) != start:
            distances[(row, col)] = dist
            continue
        for new_row, new_col in find_neighbours(matrix, row, col):
            if (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append(((new_row, new_col), dist + 1))
    return {start: distances}


def dfs_search(graph, start, end):
    stack = deque([(start, 0, {start})])
    max_distance = 0
    while stack:
        node, current_distance, visited = stack.pop()
        if node == end:
            max_distance = max(max_distance, current_distance)
            continue
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                new_distance = current_distance + weight
                new_visited = visited | {neighbor}
                stack.append((neighbor, new_distance, new_visited))
    return max_distance



def solve():
    start = (0, input[0].index("."))
    end = (len(input) - 1, input[-1].index("."))
    intersections = find_intersections(input)
    nodes = [start] + intersections + [end]
    graph = {}
    for node in nodes:
        graph |= bfs_search(input, node, nodes)

    return dfs_search(graph, start, end)

 
file_path = "input.txt"
try:
    with open(file_path, "r") as file: 
        input = file.read().strip().split('\n')
        print("Steps:", solve())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")