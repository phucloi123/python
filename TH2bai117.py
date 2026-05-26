def sum_square_subnumbers(n):
    s = str(n)
    total = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            total += int(s[i:j]) ** 2
    return total

# Test
print(sum_square_subnumbers(2207))
print(sum_square_subnumbers(54321))