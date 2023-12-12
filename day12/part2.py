"""
--- Part Two ---
As you look out at the field of springs, you feel like there are way more springs than the condition records list. When you examine the records, you discover that they were actually folded up this whole time!

To unfold the records, on each row, replace the list of spring conditions with five copies of itself (separated by ?) and replace the list of contiguous groups of damaged springs with five copies of itself (separated by ,).

So, this row:

.# 1
Would become:

.#?.#?.#?.#?.# 1,1,1,1,1
The first line of the above example would become:

???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3
In the above example, after unfolding, the number of possible arrangements for some rows is now much larger:

???.### 1,1,3 - 1 arrangement
.??..??...?##. 1,1,3 - 16384 arrangements
?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
????.#...#... 4,1,1 - 16 arrangements
????.######..#####. 1,6,5 - 2500 arrangements
?###???????? 3,2,1 - 506250 arrangements
After unfolding, adding all of the possible arrangement counts together produces 525152.

Unfold your condition records; what is the new sum of possible arrangement counts?
"""

def find_arrangements(springs, nums):
    length_num = nums[-1]
    total = 0
    if len(nums) <= 1:
        count = 0
        for x in range(0, len(springs) - length_num + 1):
            if any(char == '#' for char in springs[0 : x]):
                break
            elif any(char =='#' for char in springs[x + length_num:]):
                continue
            elif any(char in '.' for char in springs[x : x + length_num]):
                continue
            count += 1
        memo[(springs, *nums)] = count
        return count
    elif (springs, *nums) in memo:
        return memo[(springs,*nums)]
    else:
        for x in range(len(springs)-length_num, 0, -1):
            if any(char == '#' for char in springs[x + length_num:]):
                break

            elif all(char in '#?' for char in springs[x : x + length_num]):
                if springs[x - 1] == '#':
                    continue
                total += find_arrangements(springs[:x - 1], nums[:max(0,len(nums) - 1)])
        memo[(springs, *nums)] = total
        return total

def solve():
    count = 0
    for line in input.strip().split('\n'):
        springs, nums = line.split()
        nums = list(map(int, nums.split(',')))
        nums = nums * 5
        unfolded_springs = springs
        for i in range(4):
            unfolded_springs += '?' + springs
        count += find_arrangements(unfolded_springs, nums)
    return count

file_path = "input.txt"
memo = {} # using memoization
try:
    with open(file_path, "r") as file:
        input = file.read()
        print("Sum of possible arrangements:", solve())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")