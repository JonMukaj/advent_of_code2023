"""
--- Part Two ---
As you try to work out what might be wrong, the reindeer tugs on your shirt and leads you to a nearby control panel. There, a collection of buttons lets you align the contraption so that the beam enters from any edge tile and heading away from that edge. (You can choose either of two directions for the beam if it starts on a corner; for instance, if the beam starts in the bottom-right corner, it can start heading either left or upward.)

So, the beam could start on any tile in the top row (heading downward), any tile in the bottom row (heading upward), any tile in the leftmost column (heading right), or any tile in the rightmost column (heading left). To produce lava, you need to find the configuration that energizes as many tiles as possible.

In the above example, this can be achieved by starting the beam in the fourth tile from the left in the top row:

.|<2<\....
|v-v\^....
.v.v.|->>>
.v.v.v^.|.
.v.v.v^...
.v.v.v^..\
.v.v/2\\..
<-2-/vv|..
.|<<<2-|.\
.v//.|.v..
Using this configuration, 51 tiles are energized:

.#####....
.#.#.#....
.#.#.#####
.#.#.##...
.#.#.##...
.#.#.##...
.#.#####..
########..
.#######..
.#...#.#..
Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized in that configuration?
"""

from collections import deque

def solve(i, j, di, dj):
    visited = set()
    x, y = len(tiles), len(tiles[0])
    queue = deque([(i, j, di, dj)]) 
    while queue:
        i, j, di, dj = queue.popleft()
        if 0 > i or i >= x or 0 > j or j >= y or (i, j, di, dj) in visited:
            continue
        visited.add((i, j, di, dj))
        match tiles[i][j]:
            case "\\":
                queue.append((i + dj, j + di, dj, di))
            case "/":
                queue.append((i - dj, j - di, -dj, -di))
            case "|" if dj:
                queue.append((i + 1, j, 1, 0))
                queue.append((i - 1, j, -1, 0))
            case "-" if di:
                queue.append((i, j + 1, 0, 1))
                queue.append((i, j - 1, 0, -1))
            case _:
                queue.append((i + di, j + dj, di, dj))
    return len(set((i, j) for i, j, _, _ in visited))


file_path = "input.txt"
try:
    with open(file_path, "r") as file:
        tiles = file.read().strip().split("\n")
        x, y = len(tiles), len(tiles[0])
        sum = 0
        for i, j, di, dj in ([(z, 0, 0, 1) for z in range(x)] + [(z, y - 1, 0, -1) for z in range(x)] + [(0, z, 1, 0) for z in range(y)] + [(x - 1, z, -1, 0) for z in range(y)]):
            sum = max(sum, solve(i, j, di, dj))
        print("Number of energized tiles:", sum)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")