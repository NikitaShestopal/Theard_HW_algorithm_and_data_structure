def max_cyclic_shift(n: int) -> int:
    binary = bin(n)[2:]
    max_val = n

    for _ in range(len(binary) - 1):
        binary = binary[1:] + binary[0]
        max_val = max(max_val, int(binary, 2))

    return max_val

n = int(input())
print(max_cyclic_shift(n))
