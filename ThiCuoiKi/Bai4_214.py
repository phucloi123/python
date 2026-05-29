# Bai4_214.py - Anonymous lambda functions, filter 1-10000
import math

# Ham lambda kiem tra so chinh phuong
# Lay can bac hai roi binh phuong lai, neu bang n thi la so chinh phuong
is_perfect_square = lambda n: int(math.sqrt(n)) ** 2 == n

# Ham lambda kiem tra so hoan thien (perfect number)
# So hoan thien: tong cac uoc so (khong ke chinh no) bang chinh no
is_perfect_number = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) == n


print("\n=== So chinh phuong (Perfect squares) 1-10000 ===")
perfect_squares = list(filter(is_perfect_square, range(1, 10001)))
print(perfect_squares)

print("\n=== So hoan thien (Perfect numbers) 1-10000 ===")
perfect_numbers = list(filter(is_perfect_number, range(1, 10001)))
print(perfect_numbers)