from math import gcd

def is_friendly(n):
    rev = int(str(n)[::-1])   # đảo ngược số
    return gcd(n, rev) == 1

def find_friendly_numbers(a, b):
    result = [n for n in range(a, b + 1) if is_friendly(n)]
    print(f"Các số thân thiện trong [{a}, {b}]:")
    print(result)
    print(f"Số lượng: {len(result)}")

# Test
find_friendly_numbers(10, 100)