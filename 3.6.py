import sys

def search(have, sby):
    for i in have:
        for k in sby:
            if i == k:
                print("YES")
            else:
                print("NO")


lines = sys.stdin.read().strip().split("\n")
index = 0

while index < len(lines):
    n = int(lines[index])
    have = list(map(int, lines[index + 1].split()))
    l = int(lines[index])
    sby = list(map(int, lines[index + 3].split()))
    print(search(have, sby))
    index += 4
