import bisect


def search(data_list_first, data_list_second):
    s = []
    for k in data_list_second:
        left = bisect.bisect_left(data_list_first, k)
        right = bisect.bisect_right(data_list_first, k)
        s.append(right - left)
    return s

n = int(input())
data_list_first = list(map(int, input().split()))
m = int(input())
data_list_second = list(map(int, input().split()))

print("\n".join(map(str, search(data_list_first, data_list_second))))
