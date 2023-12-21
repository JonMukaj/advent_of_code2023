"""
--- Part Two ---
The Elf seems confused by your answer until he realizes his mistake: he was reading from a list of his favorite numbers that are both perfect squares and perfect cubes, not his step counter.

The actual number of steps he needs to get today is exactly 26501365.

He also points out that the garden plots and rocks are set up so that the map repeats infinitely in every direction.

So, if you were to look one additional map-width or map-height out from the edge of the example map above, you would find that it keeps repeating:

.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##..S####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
This is just a tiny three-map-by-three-map slice of the inexplicably-infinite farm layout; garden plots and rocks repeat as far as you can see. The Elf still starts on the one middle tile marked S, though - every other repeated S is replaced with a normal garden plot (.).

Here are the number of reachable garden plots in this new infinite version of the example map for different numbers of steps:

In exactly 6 steps, he can still reach 16 garden plots.
In exactly 10 steps, he can reach any of 50 garden plots.
In exactly 50 steps, he can reach 1594 garden plots.
In exactly 100 steps, he can reach 6536 garden plots.
In exactly 500 steps, he can reach 167004 garden plots.
In exactly 1000 steps, he can reach 668697 garden plots.
In exactly 5000 steps, he can reach 16733044 garden plots.
However, the step count the Elf needs is much larger! Starting from the garden plot marked S on your infinite map, how many garden plots could the Elf reach in exactly 26501365 steps?
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
    history, _ = generate_history(grid, start, maxX, maxY, 3*262+65)
    steps = 101150
    a = history[2*262+65]
    b = history[2*262+65] - history[262+65]
    c = history[3*262+65] - 2*history[2*262+65] + history[262+65]
    total = a + b*(steps-2) + c*((steps-2)*(steps-1)//2)
    return total

file_path = "input.txt"
try:
    with open(file_path, "r") as file: 
        input = file.read()
        print("Nr of garden plots:", solve())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")