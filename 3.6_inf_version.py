import sys
import bisect

def search(have, sby):
    for k in sby:
        idx = bisect.bisect_left(have, k)
        if idx < len(have) and have[idx] == k:
            print("YES")
        else:
            print("NO")

lines = sys.stdin.read().strip().split("\n")
index = 0

while index < len(lines):
    n = int(lines[index])
    have = list(map(int, lines[index + 1].split()))
    m = int(lines[index + 2])
    sby = list(map(int, lines[index + 3].split()))
    search(have, sby)
    index += 4