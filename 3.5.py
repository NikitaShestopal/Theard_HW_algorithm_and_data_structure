def olympiad_sort(numbers, min_value, max_value):
    s = 0
    for i in numbers:
        if max_value > i > min_value:
            s += 1
    return s


n = int(input())
numbers = list(map(int, input().split()))
values = list(map(int, input().split()))
print(olympiad_sort(numbers, values[0], values[1]))