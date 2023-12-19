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

import re

def return_nums(s):
	return list(map(int, re.findall(r'\d+', s)))

def both(char, greater, value, ranges):
	char = 'xmas'.index(char)
	new_ranges = []
	for r in ranges:
		r = list(r)
		lower, higher = r[char]
		if greater:
			lower = max(lower, value + 1)
		else:
			higher = min(higher, value - 1)
		if lower > higher:
			continue
		r[char] = (lower, higher)
		new_ranges.append(tuple(r))
	return new_ranges


def outer_ranges(work):
	return inner_ranges(workflow[work].split(","))

def inner_ranges(w):
	i = w[0]
	if i == "R":
		return []
	if i == "A":
		return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
	if ":" not in i:
		return outer_ranges(i)
	condition = i.split(":")[0]
	greater = ">" in condition
	char = condition[0]
	value = int(condition[2:])
	inverted_value = value + 1 if greater else value - 1
	true_condition = both(char, greater, value, inner_ranges([i.split(":")[1]]))
	false_condition = both(char, not greater, inverted_value, inner_ranges(w[1:]))
	return true_condition + false_condition

def solve():
  sum = 0
  for range in outer_ranges('in'):
    v = 1
    for lower, higher in range:
      v *= higher - lower + 1
    sum += v
  return sum


file_path = "input.txt"
try:
    with open(file_path, "r") as file:
        input = file.read()
        system = [s for s in input.strip().split('\n\n')]
        workflow, parts = system
        parts = [return_nums(p) for p in parts.split("\n")]
        workflow = {w.split("{")[0]: w.split("{")[1][:-1] for w in workflow.split("\n")}
        print("Sum:", solve())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")