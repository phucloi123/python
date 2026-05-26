# ==================== FUNCTIONS ====================

def print_multiplication_tables(a: int, b: int):
    step = 1 if a <= b else -1
    for i in range(a, b + step, step):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()

#kiem tra so nguyen to
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def list_primes_less_than(n: int):
    primes = [i for i in range(2, n) if is_prime(i)]
    if primes:
        print(f"Primes < {n}: {primes}")
    else:
        print(f"No primes < {n}")


def count_primes_less_than(n: int):
    count = sum(1 for i in range(2, n) if is_prime(i))
    print(f"Count of primes < {n}: {count}")


def list_prime_divisors(n: int):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    prime_divisors = [i for i in divisors if is_prime(i)]
    print(f"All divisors of {n}:          {divisors}")
    print(f"Prime divisors of {n}: {prime_divisors}")


# ==================== MENU ====================

def menu():
    while True:
        print("\n========== MENU ==========")
        print("1. Bang cuu chuong (a va b)")
        print("2. Kiem tra so nguyen to")
        print("3. liet ke so < n")
        print("4. Dem so nguyen to < n")
        print("5. liet ke cac uoc so nguyen to n")
        print("0. Thoat")
        print("==========================")

        choice = input("Chon: ").strip()

        match choice:
            case "1":
                a, b = map(int, input("Enter a, b (e.g: 2,5): ").split(","))
                print_multiplication_tables(a, b)

            case "2":
                n = int(input("Enter n: "))
                result = "IS prime" if is_prime(n) else "is NOT prime"
                print(f"{n} {result}.")

            case "3":
                n = int(input("Enter n: "))
                list_primes_less_than(n)

            case "4":
                n = int(input("Enter n: "))
                count_primes_less_than(n)

            case "5":
                n = int(input("Enter n: "))
                list_prime_divisors(n)

            case "0":
                print("Goodbye!")
                break

            case _:
                print("Invalid choice, try again.")
menu()