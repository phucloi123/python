def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1): # can bat 2 de toi ua so nguyen to
        if n % i == 0:
            return False
    return True

def main():
    numbers = []

    while True:
        num = int(input("Enter an integer: "))
        numbers.append(num)

        choise = input("Do you want to continue (Y/N): ").strip().upper()
        if choise == "N":
            break

    print(f"List: {numbers}")

    #a So nguyen to
    prime = [n for n in numbers if is_prime(n)]
    print(f"a) So nguyen to: {prime}")

    #b trung binh so am / duong
    negatives = [n for n in numbers if n < 0]
    positives = [n for n in numbers if n > 0]

    avg_neg = sum(negatives) / len(negatives) if negatives else None
    avg_pos = sum(positives) / len(positives) if positives else None

    print(f"\nb) Average of negatives: {avg_neg if avg_neg is not None else 'No negative numbers'}")
    print(f"   Average of positives: {avg_pos if avg_pos is not None else 'No positive numbers'}")

    # c) lớn nhất, nhỏ nhất
    print(f"\nc) Max: {max(numbers)}")
    print(f"   Min: {min(numbers)}")

    # d) kiểm tra sắp xếp tăng dần
    is_sorted = all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
    print(f"\nd) Is sorted ascending: {'Yes' if is_sorted else 'No'}")

main()