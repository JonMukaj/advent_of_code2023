"""
--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""

def is_symbol(char):
    return char in ['-','^','!','&','*', '#', '+', '$', '/', '@', '%', '=']

def get_adjacent_indices(row, col, rows, cols):
    indices = []
    for i in range(max(0, row - 1), min(row + 2, rows)):
        for j in range(max(0, col - 1), min(col + 2, cols)):
            if i != row or j != col:
                indices.append((i, j))

    return indices

def get_num_info(num_map, i):
    return int("".join(num_map.values())), min(num_map), max(num_map), i

def sum_of_parts(engine_schematic):
    rows = len(engine_schematic)
    cols = len(engine_schematic[0])
    
    number_maps = {}
    
    for i, line in enumerate(engine_schematic):
        number_map = []
        digit_map = {}
        for pos, char in enumerate(line):
            if char.isdigit():
                digit_map[pos] = char
            else:
                if len(digit_map) != 0:
                    number_map.append(digit_map)
                digit_map = {}
        number_maps[i] = number_map

    gear_locations = set()
    list_of_nums = set()
    for i, row_of_num in number_maps.items():
        for num_map in row_of_num:
            positions = list(num_map.keys())
            for pos in positions:
                for k, l in get_adjacent_indices(i, pos, rows, cols):
                    if is_symbol(engine_schematic[k][l]):
                        if engine_schematic[k][l] == "*":
                            gear_locations.add((k,l))
                            list_of_nums.add(get_num_info(num_map, i))

    sum_of_gear_ratios = 0
    for x, y in gear_locations:
        gear_borders = set()
        gear_neighbors = []
        for k in range(x-1,x+2):
            for l in range(y-1,y+2):
                gear_borders.add((k,l))
        
        for num, x1, x2, y in list_of_nums:
            if (y, x1) in gear_borders or (y, x2) in gear_borders:
                gear_neighbors.append(num)
        if len(gear_neighbors) == 2:
            sum_of_gear_ratios += gear_neighbors[0]*gear_neighbors[1]
    return sum_of_gear_ratios

file_path = "input.txt"
try:
    with open(file_path, "r") as file:
        input = file.readlines()
        print("The sum of all gear ratios is:", sum_of_parts(input))
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")