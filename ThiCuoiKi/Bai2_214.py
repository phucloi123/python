# Bai2_214.py - Prime number functions

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_less_than(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count

def get_all_divisors(n):
    # Lay tat ca uoc so cua n (bao gom ca 1 va n)
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

def prime_divisors(n):
    result = []
    # Chi giu lai cac uoc so la so nguyen to
    for i in range(1, n + 1):
        if n % i == 0 and is_prime(i):
            result.append(i)
    return result

# ---- Chuong trinh chinh ----
n = int(input("Nhap so nguyen duong n: "))

# Cau 1: Kiem tra n co phai so nguyen to khong
print(f"{n} {'la' if is_prime(n) else 'khong la'} so nguyen to")

# Cau 2: Dem so nguyen to nho hon n
count = count_primes_less_than(n)
print(f"So luong so nguyen to < {n}: {count}")

# Cau 3: In tat ca uoc so truoc, sau do in rieng cac uoc so la so nguyen to
all_divs = get_all_divisors(n)
prime_divs = prime_divisors(n)

print(f"Cac uoc so cua {n} gom: {','.join(map(str, all_divs))}")
print(f"Cac so vua la uoc so cua {n}, vua la so nguyen to: {','.join(map(str, prime_divs))}")