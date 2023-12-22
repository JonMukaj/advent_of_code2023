"""
--- Part Two ---
Disintegrating bricks one at a time isn't going to be fast enough. While it might sound dangerous, what you really need is a chain reaction.

You'll need to figure out the best brick to disintegrate. For each brick, determine how many other bricks would fall if that brick were disintegrated.

Using the same example as above:

Disintegrating brick A would cause all 6 other bricks to fall.
Disintegrating brick F would cause only 1 other brick, G, to fall.
Disintegrating any other brick would cause no other bricks to fall. So, in this example, the sum of the number of other bricks that would fall as a result of disintegrating each brick is 7.

For each brick, determine how many other bricks would fall if that brick were disintegrated. What is the sum of the number of other bricks that would fall?
"""

from collections import defaultdict
import re

def check_down(brick):
	return (brick[0], brick[1], brick[2] - 1, brick[3], brick[4], brick[5] - 1, brick[6])

def positions(brick):
	for x in range(brick[0], brick[3] + 1):
		for y in range(brick[1], brick[4] + 1):
			for z in range(brick[2], brick[5] + 1):
				yield (x,y,z)

def is_falling(brick, falling, above, below):
	if brick in falling:
		return
	falling.add(brick)
	for parent in above[brick]:
		if not len(below[parent] - falling):
			is_falling(parent, falling, above, below)
                        
def check_condition(disintegrated, above, below):
	falling = set()
	is_falling(disintegrated, falling, above, below)
	return len(falling)

def get_nums(s):
	return list(map(int, re.findall(r'\d+', s)))

def solve():
    total = 0
    blocks = [tuple(get_nums(x) + [i]) for i, x in enumerate(input)]
    occupied = {}
    fallen = []
    for brick in sorted(blocks, key=lambda brick: brick[2]):
        while brick[2] > 0 and all(pos not in occupied for pos in positions(check_down(brick))):
            brick = check_down(brick)
        for pos in positions(brick):
            occupied[pos] = brick
        fallen.append(brick)    
    above = defaultdict(set)
    below = defaultdict(set)
    for brick in fallen:
        inthisbrick = set(positions(brick))
        for pos in positions(check_down(brick)):
            if pos in occupied and pos not in inthisbrick:
                above[occupied[pos]].add(brick)
                below[brick].add(occupied[pos])
    for brick in fallen:
        fall = check_condition(brick, above, below)
        total += fall - 1
    return total
        
file_path = "input.txt"
try:
    with open(file_path, "r") as file: 
        input = file.read().strip().split('\n')
        print("Nr of other falling bricks:", solve())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")