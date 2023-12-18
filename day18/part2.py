"""
--- Part Two ---
The Elves were right to be concerned; the planned lagoon would be much too small.

After a few minutes, someone realizes what happened; someone swapped the color and instruction parameters when producing the dig plan. They don't have time to fix the bug; one of them asks if you can extract the correct instructions from the hexadecimal codes.

Each hexadecimal code is six hexadecimal digits long. The first five hexadecimal digits encode the distance in meters as a five-digit hexadecimal number. The last hexadecimal digit encodes the direction to dig: 0 means R, 1 means D, 2 means L, and 3 means U.

So, in the above example, the hexadecimal codes can be converted into the true instructions:

#70c710 = R 461937
#0dc571 = D 56407
#5713f0 = R 356671
#d2c081 = D 863240
#59c680 = R 367720
#411b91 = D 266681
#8ceee2 = L 577262
#caa173 = U 829975
#1b58a2 = L 112010
#caa171 = D 829975
#7807d2 = L 491645
#a77fa3 = U 686074
#015232 = L 5411
#7a21e3 = U 500254
Digging out this loop and its interior produces a lagoon that can hold an impressive 952408144115 cubic meters of lava.

Convert the hexadecimal color codes into the correct instructions; if the Elves follow this new dig plan, how many cubic meters of lava could the lagoon hold?
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
    dir_inst = ['R','D','L','U']
    instrs = []
    for _, ins in enumerate(dig_plan):
        hexinst = ins.split()[2].strip('(').strip(')')
        steps = str(int(hexinst[1:6],16))
        instrs.append(dir_inst[int(hexinst[-1])]+' '+steps)
    cur = (0,0)
    corners, conc_corners, conv_corners, perimeter = process(instrs, cur)
    total_a = find_area(corners)
    return int(perimeter + (total_a - conc_corners/4 - conv_corners*3/4 - (perimeter-len(corners))/2))


file_path = "input.txt"
try:
    with open(file_path, "r") as file:
        input = file.readlines()
        print("Cubic meters:", solve())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")