"""
--- Day 18: Lavaduct Lagoon ---
Thanks to your efforts, the machine parts factory is one of the first factories up and running since the lavafall came back. However, to catch up with the large backlog of parts requests, the factory will also need a large supply of lava for a while; the Elves have already started creating a large lagoon nearby for this purpose.

However, they aren't sure the lagoon will be big enough; they've asked you to take a look at the dig plan (your puzzle input). For example:

R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
The digger starts in a 1 meter cube hole in the ground. They then dig the specified number of meters up (U), down (D), left (L), or right (R), clearing full 1 meter cubes as they go. The directions are given as seen from above, so if "up" were north, then "right" would be east, and so on. Each trench is also listed with the color that the edge of the trench should be painted as an RGB hexadecimal color code.

When viewed from above, the above example dig plan would result in the following loop of trench (#) having been dug out from otherwise ground-level terrain (.):

#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######
At this point, the trench could contain 38 cubic meters of lava. However, this is just the edge of the lagoon; the next step is to dig out the interior so that it is one meter deep as well:

#######
#######
#######
..#####
..#####
#######
#####..
#######
.######
.######
Now, the lagoon can contain a much more respectable 62 cubic meters of lava. While the interior is dug out, the edges are also painted according to the color codes in the dig plan.

The Elves are concerned the lagoon won't be large enough; if they follow their dig plan, how many cubic meters of lava could it hold?
"""


def process(dig_plan, start):
  instrs = dig_plan.copy()
  dirs = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
  cur = start
  corners = []
  conc_corners = 0
  conv_corners = 0
  prevDir = dig_plan[-1].split()[0]
  perimeter = 0
  for inst in instrs:
    corners.append(cur)
    inst_split = inst.split()
    curDir = inst_split[0]
    steps = int(inst_split[1])
    cur = (cur[0] + dirs[curDir][0] * steps,cur[1] + dirs[curDir][1] * steps)
    if (prevDir == 'U' and curDir == 'R') or (prevDir == 'L' and curDir == 'U') or (prevDir == 'D' and curDir == 'L') or (prevDir == 'R' and curDir == 'D'):
      conc_corners += 1
    elif (prevDir == 'U' and curDir == 'L') or (prevDir == 'L' and curDir == 'D') or (prevDir == 'D' and curDir == 'R') or (prevDir == 'R' and curDir == 'U'):
      conv_corners += 1
    prevDir = curDir
    perimeter += steps
  return corners, conc_corners, conv_corners, perimeter

def find_area(corners):
    n = len(corners)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area


def solve():
    dig_plan = [line.strip('\n') for line in input]
    cur = (0,0)
    corners, conc_corners, conv_corners, perimeter = process(dig_plan, cur)
    total_a = find_area(corners)
    return int(perimeter + (total_a - conc_corners/4 - conv_corners*3/4 - (perimeter-len(corners))/2))


file_path = "input.txt"
try:
    with open(file_path, "r") as file:
        input = file.readlines()
        print("Cubic meters:", solve())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")