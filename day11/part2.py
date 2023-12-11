"""
--- Part Two ---
The galaxies are much older (and thus much farther apart) than the researcher initially estimated.

Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.

(In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)

Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
"""

def find_distances(pair):
    sum_list = []
    for p in pair:
        sum = 0
        for i in range(p):
            sum += 1 if i in pair else 1000000
        sum_list.append(sum)
    sum = 0
    for x in sum_list:
        for y in sum_list:
            sum += abs(x - y)
    return sum//2

def solve():
    x, y = [], []
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if char == '#':
                x.append(j)
                y.append(i)
    return sum(map(find_distances, [x, y]))
    

file_path = "input.txt"
try:
    with open(file_path, "r") as file:
        input = file.readlines()
        print("Sum of lengths:", solve())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")