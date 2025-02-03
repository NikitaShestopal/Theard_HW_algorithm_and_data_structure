import bisect

def search(have, sby):
    for k in sby:
        idx = bisect.bisect_left(have, k)
        if idx < len(have) and have[idx] == k:
            print("YES")
        else:
            print("NO")

n = int(input())
have = list(map(int, input().split()))
m = int(input())
sby = list(map(int, input().split()))

search(have, sby)
