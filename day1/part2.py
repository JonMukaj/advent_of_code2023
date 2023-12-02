
"""
--- Day 1: Trebuchet?! ---
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
"""

def preprocess_line(line):
    spelled_out_digits = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for spelled_out, numeric in spelled_out_digits.items():
        line = line.replace(spelled_out, f'{spelled_out}{numeric}{spelled_out}')
    return line

def extract_calibration_value(line):
    start, end = 0, len(line) - 1

    # Find the first digit
    while start < len(line) and not line[start].isdigit():
        start += 1

    # Find the last digit
    while end >= 0 and not line[end].isdigit():
        end -= 1

    # If at least one digit is found
    if start < len(line) and end >= 0:
        first_digit = int(line[start])
        last_digit = int(line[end])

        # Form a two-digit number
        calibration_value = int(str(first_digit) + str(last_digit))
        return calibration_value
    else:
        return 0

def sum_calibration_values(calibration_document):
    calibration_values = [extract_calibration_value(preprocess_line(line.strip())) for line in calibration_document]
    total_sum = sum(calibration_values)
    return total_sum

file_path = "calibration_input.txt"

try:
    with open(file_path, "r") as file:
        calibration_document = file.readlines()
    result = sum_calibration_values(calibration_document)
    print("The sum of calibration values is:", result)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")