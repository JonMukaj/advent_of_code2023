"""
--- Part Two ---
The crucibles of lava simply aren't large enough to provide an adequate supply of lava to the machine parts factory. Instead, the Elves are going to upgrade to ultra crucibles.

Ultra crucibles are even more difficult to steer than normal crucibles. Not only do they have trouble going in a straight line, but they also have trouble turning!

Once an ultra crucible starts moving in a direction, it needs to move a minimum of four blocks in that direction before it can turn (or even before it can stop at the end). However, it will eventually start to get wobbly: an ultra crucible can move a maximum of ten consecutive blocks without turning.

In the above example, an ultra crucible could follow this path to minimize heat loss:

2>>>>>>>>1323
32154535v5623
32552456v4254
34465858v5452
45466578v>>>>
143859879845v
445787698776v
363787797965v
465496798688v
456467998645v
122468686556v
254654888773v
432267465553v
In the above example, an ultra crucible would incur the minimum possible heat loss of 94.

Here's another example:

111111111111
999999999991
999999999991
999999999991
999999999991
Sadly, an ultra crucible would need to take an unfortunate path like this one:

1>>>>>>>1111
9999999v9991
9999999v9991
9999999v9991
9999999v>>>>
This route causes the ultra crucible to incur the minimum possible heat loss of 71.

Directing the ultra crucible from the lava pool to the machine parts factory, what is the least heat loss it can incur?
"""

import heapq

def solve(start, end, min_moves, most_moves):
    visited = set()
    queue = [(0, *start, 0, 0)]
    while queue:
        heat, x, y, px, py = heapq.heappop(queue)
        if (x, y) == end: 
            return heat
        if (x, y, px, py) in visited: 
            continue
        visited.add((x, y, px, py))

        for dx,dy in {(1,0), (0,1), (-1,0), (0,-1)} - {(px, py), (-px, -py)}:
            a, b, c = x, y, heat
            for i in range(1, most_moves + 1):
                a, b = a + dx, b + dy
                if (a,b) in input:
                    c += input[a, b]
                    if i >= min_moves:
                        heapq.heappush(queue, (c, a, b, dx, dy))

file_path = "input.txt"
try:
    with open(file_path, "r") as file:
        input = {(i, j): int(b) for i, a in enumerate(file) for j, b in enumerate(a.strip())}
        print("Least heat loss:", solve((0, 0), max(input), 4, 10))
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")