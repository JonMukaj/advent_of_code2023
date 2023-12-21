"""
--- Day 21: Step Counter ---
You manage to catch the airship right as it's dropping someone else off on their all-expenses-paid trip to Desert Island! It even helpfully drops you off near the gardener and his massive farm.

"You got the sand flowing again! Great work! Now we just need to wait until we have enough sand to filter the water for Snow Island and we'll have snow again in no time."

While you wait, one of the Elves that works with the gardener heard how good you are at solving problems and would like your help. He needs to get his steps in for the day, and so he'd like to know which garden plots he can reach with exactly his remaining 64 steps.

He gives you an up-to-date map (your puzzle input) of his starting position (S), garden plots (.), and rocks (#). For example:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
The Elf starts at the starting position (S) which also counts as a garden plot. Then, he can take one step north, south, east, or west, but only onto tiles that are garden plots. This would allow him to reach any of the tiles marked O:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#O#....
.##.OS####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
Then, he takes a second step. Since at this point he could be at either tile marked O, his second step would allow him to reach any garden plot that is one step north, south, east, or west of any tile that he could have reached after the first step:

...........
.....###.#.
.###.##..#.
..#.#O..#..
....#.#....
.##O.O####.
.##.O#...#.
.......##..
.##.#.####.
.##..##.##.
...........
After two steps, he could be at any of the tiles marked O above, including the starting position (either by going north-then-south or by going west-then-east).

A single third step leads to even more possibilities:

...........
.....###.#.
.###.##..#.
..#.#.O.#..
...O#O#....
.##.OS####.
.##O.#...#.
....O..##..
.##.#.####.
.##..##.##.
...........
He will continue like this until his steps for the day have been exhausted. After a total of 6 steps, he could reach any of the garden plots marked O:

...........
.....###.#.
.###.##.O#.
.O#O#O.O#..
O.O.#.#.O..
.##O.O####.
.##.O#O..#.
.O.O.O.##..
.##.#.####.
.##O.##.##.
...........
In this example, if the Elf's goal was to get exactly 6 more steps today, he could use them to reach any of 16 garden plots.

However, the Elf actually needs to get 64 steps today, and the map he's handed you is much larger than the example map.

Starting from the garden plot marked S on your map, how many garden plots could the Elf reach in exactly 64 steps?
"""

def infinite_grid(grid, p, maxX, maxY):
    x = p.real % (maxX + 1)
    y = p.imag % (maxY + 1)
    return grid[x + y * 1j]

def generate_history(grid, start, maxX, maxY, steps):
    odds, evens, queue = set(), {start}, {start}
    n4 = lambda p: [p - 1j, p - 1, p + 1, p + 1j]
    odd_history, even_history = [0], [0]
    for i in range(1,steps+1):
        new_points = set()
        for p in queue:
            for n in [n for n in n4(p) if n not in evens and n not in odds]:
                if infinite_grid(grid, n, maxX, maxY) in ".S":
                    new_points.add(n)
        if i % 2:
            odds |= new_points
        else:
            evens |= new_points
        odd_history.append(len(odds))
        even_history.append(len(evens))
        queue = new_points
    return odd_history, even_history

def solve():
    grid, start = {}, None
    for y, line in enumerate(input.split("\n")):
        for x, c in enumerate(line):
            if c == "S":
                start = x + 1j * y
            grid[x + 1j * y] = c
    maxX, maxY = int(max(p.real for p in grid)), int(max(p.imag for p in grid))
    _, even_history = generate_history(grid, start, maxX, maxY, 64)
    return even_history[-1]   

file_path = "input.txt"
try:
    with open(file_path, "r") as file: 
        input = file.read()
        print("Nr of garden plots:", solve())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")