import sys

def olympiad_sort(numbers, min_value, max_value):
    return sum(min_value <= i <= max_value for i in numbers)


lines = sys.stdin.read().strip().split("\n")
index = 0

while index < len(lines):
        n = int(lines[index])
        numbers = list(map(int, lines[index + 1].split()))
        values = list(map(int, lines[index + 2].split()))
        print(olympiad_sort(numbers, values[0], values[1]))
        index += 3
