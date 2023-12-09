"""
--- Part Two ---
Of course, it would be nice to have even more history included in your report. Surely it's safe to just extrapolate backwards as well, right?

For each history, repeat the process of finding differences until the sequence of differences is entirely zero. Then, rather than adding a zero to the end and filling in the next values of each previous sequence, you should instead add a zero to the beginning of your sequence of zeroes, then fill in new first values for each previous sequence.

In particular, here is what the third example history looks like when extrapolating back in time:

5  10  13  16  21  30  45
  5   3   3   5   9  15
   -2   0   2   4   6
      2   2   2   2
        0   0   0
Adding the new values on the left side of each sequence from bottom to top eventually reveals the new left-most history value: 5.

Doing this for the remaining example data above results in previous values of -3 for the first history and 0 for the second history. Adding all three new values together produces 2.

Analyze your OASIS report again, this time extrapolating the previous value for each history. What is the sum of these extrapolated values?
"""

def divided_difference(x, y):
    n = len(x)
    F = [[None] * n for _ in range(n)]
    for i in range(n):
        F[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x[i + j] - x[i])
    return F

def newton_interpolation(interpolate_value, x, F):
    n = len(x)
    result = F[0][0]

    for j in range(1, n):
        term = 1
        for i in range(j):
            term *= (interpolate_value - x[i])
        result += F[0][j] * term

    return round(result)

def solve():
    sum = []
    for line in input:
        y = list(map(int, line.strip().split()))
        x = list(range(len(y)))
        F = divided_difference(x, y)
        sum.append(newton_interpolation(-1, x, F)) 
    return sum
        
file_path = "input.txt"
try:
    with open(file_path, "r") as file:
        input = file.readlines()
        print("Sum of the extrapolated values:", sum(solve()))
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")