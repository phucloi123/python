import math
#So than thien
# n va so dao nguoc co GCD = 1
is_than_thien = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

#b So chinh phuong
is_So_Chinh_Phuong = lambda n: math.isqrt(n) ** 2 == n

# C) so dong nhat
# cach 1: dung all()
is_so_dong_nhat_all = lambda n: all(c == str(n)[0] for c in str(n))

#cach 2 : dung any()
is_so_dong_nhat_any = lambda n: any(c == str(n)[0] for c in str(n))

#in ket qua tu 1 den 1.000.000

LIMIT = 1_000_000

print("=== a) So than thien ( 1 -> 1000000) ===")
result = [n for n in range(1, LIMIT + 1) if is_than_thien(n)]
print(result[:20])

print("=== b) So chinh phuong ( 1 -> 1000000) ===")
result = [n for n in range(1, LIMIT + 1) if is_than_thien(n)]
print(result)

print("=== c) So dong nhat - cach 1 dung all() ( 1 -> 1000000) ===")
result = [n for n in range(1, LIMIT + 1) if is_so_dong_nhat_all(n)]
print(result)

print("=== c) So dong nhat - cach 2 dung any() ( 1 -> 1000000) ===")
result = [n for n in range(1, LIMIT + 1) if is_so_dong_nhat_any(n)]
print(result)

# ── Cách thường: O(n) mỗi số → tổng O(n²) ──────────────────────────────────
is_hoan_thien_slow = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

# ── Cách tối ưu: O(√n) mỗi số ───────────────────────────────────────────────
def sum_proper_divisors(n):
    if n < 2:
        return 0
    total = 1  # 1 always divides n
    sqrt_n = math.isqrt(n)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total += i
            if i != n // i:          # avoid counting sqrt twice (e.g. 36: i=6, n//i=6)
                total += n // i
    return total

is_hoan_thien_fast = lambda n: n > 1 and sum_proper_divisors(n) == n


# ── Benchmark so sánh ────────────────────────────────────────────────────────
import time

LIMIT = 1_000_000

start = time.time()
slow_result = [n for n in range(1, LIMIT + 1) if is_hoan_thien_slow(n)]
print(f"Slow: {time.time() - start:.2f}s → {slow_result}")

start = time.time()
fast_result = [n for n in range(1, LIMIT + 1) if is_hoan_thien_fast(n)]
print(f"Fast: {time.time() - start:.2f}s → {fast_result}")