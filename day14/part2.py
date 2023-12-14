"""
--- Part Two ---
The parabolic reflector dish deforms, but not in a way that focuses the beam. To do that, you'll need to move the rocks to the edges of the platform. Fortunately, a button on the side of the control panel labeled "spin cycle" attempts to do just that!

Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east. After each tilt, the rounded rocks roll as far as they can before the platform tilts in the next direction. After one cycle, the platform will have finished rolling the rounded rocks in those four directions in that order.

Here's what happens in the example above after each of the first few cycles:

After 1 cycle:
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....

After 2 cycles:
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O

After 3 cycles:
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O
This process should work if you leave it running long enough, but you're still worried about the north support beams. To make sure they'll survive for a while, you need to calculate the total load on the north support beams after 1000000000 cycles.

In the above example, after 1000000000 cycles, the total load on the north support beams is 64.

Run the spin cycle for 1000000000 cycles. Afterward, what is the total load on the north support beams?
"""

def push_rocks(row):
    count = 0
    for i, element in enumerate(row):
        if element == '#' and count > 0:
            for j in range(i - count, i):
                row[j] = 'O'
            count = 0
        elif element == 'O':
            count += 1
            row[i] = '.'

        if i == len(row) - 1 and count > 0:
            for k in range(len(row) - count, len(row)):
                row[k] = 'O'
            count = 0
    return row


def transpose_clockwise(platform):
    return list(map(lambda x: "".join(reversed(x)), zip(*platform)))

def transpose_counterclockwise(platform):
    new_platform = []
    for x in reversed(list(zip(*platform))):
        new_platform.append("".join(x))
    return new_platform

def tilt_north(platform):
    return (transpose_counterclockwise(tilt_east(transpose_clockwise(platform))))

def tilt_east(platform):
    new_platform = []
    for row in platform:
        new_platform.append("".join(push_rocks(list(row))))
    return new_platform

def tilt_west(platform):
    new_platform = []
    for x in (tilt_east(["".join(reversed(x)) for x in platform])):
        new_platform.append("".join(reversed(x)))
    return new_platform

def tilt_south(platform):
    return (transpose_clockwise(tilt_east(transpose_counterclockwise(platform))))


def calculate_load(platform):
    load = 0
    for i, row in enumerate(platform):
        load += row.count("O") * (len(platform) - i)
    return load

def spin_cycle(platform):
    return tilt_east(tilt_south(tilt_west(tilt_north(platform))))

def solve():
    platform = [line for line in input.strip().split("\n")]
    num_of_cycles = 1000
    iterations = 0
    while iterations < num_of_cycles:
        platform = spin_cycle(platform)
        iterations += 1

    return calculate_load(platform)


file_path = "input.txt"
try:
    with open(file_path, "r") as file:
        input = file.read()
        print("Total load with cycles:", solve())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")