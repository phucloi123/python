import math

# ==================== LAMBDA FUNCTIONS ====================

# Bài 1: Trị tuyệt đối
absolute = lambda n: abs(n)

# Bài 2: n + 15
plus_fifteen = lambda n: n + 15

# Bài 3: Tích x * y
product = lambda x, y: x * y

# Bài 4: Bội số của 13 hoặc 19
is_multiple_13_or_19 = lambda n: n % 13 == 0 or n % 19 == 0

# Bài 5: Diện tích hình tròn
circle_area = lambda r: math.pi * r ** 2

# Bài 6: Chu vi hình chữ nhật
rectangle_perimeter = lambda d, r: 2 * (d + r)

# Bài 7: Số chính phương
is_perfect_square = lambda n: n >= 0 and int(math.sqrt(n)) ** 2 == n

# Bài 8: Số nguyên tố
is_prime = lambda n: n >= 2 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# Bài 9: Kiểm tra tam giác
def classify_triangle(a, b, c):
    # Check if valid triangle (điều kiện hợp lệ)
    is_valid = lambda a, b, c: a + b > c and a + c > b and b + c > a

    if not is_valid(a, b, c):
        return "Không tạo thành tam giác."

    is_equilateral  = lambda a, b, c: a == b == c                          # đều
    is_isosceles    = lambda a, b, c: a == b or b == c or a == c           # cân
    is_right        = lambda a, b, c: sorted([a**2, b**2, c**2])[-1] == sum(sorted([a**2, b**2, c**2])[:2])  # vuông

    if is_equilateral(a, b, c):
        return "Tam giác ĐỀU."
    elif is_right(a, b, c) and is_isosceles(a, b, c):
        return "Tam giác CÂN VUÔNG."
    elif is_right(a, b, c):
        return "Tam giác VUÔNG."
    elif is_isosceles(a, b, c):
        return "Tam giác CÂN."
    else:
        return "Tam giác THƯỜNG."


# ==================== MENU ====================

def menu():
    while True:
        print("\n========== MENU ==========")
        print("1.  Trị tuyệt đối của n")
        print("2.  Giá trị n + 15")
        print("3.  Tích của x và y")
        print("4.  Kiểm tra bội số của 13 hoặc 19")
        print("5.  Diện tích hình tròn")
        print("6.  Chu vi hình chữ nhật")
        print("7.  Kiểm tra số chính phương")
        print("8.  Kiểm tra số nguyên tố")
        print("9.  Phân loại tam giác")
        print("0.  Thoát")
        print("==========================")

        choice = input("Chọn: ").strip()

        match choice:
            case "1":
                n = int(input("Nhập n: "))
                print(f"Trị tuyệt đối của {n} = {absolute(n)}")

            case "2":
                n = int(input("Nhập n: "))
                print(f"{n} + 15 = {plus_fifteen(n)}")

            case "3":
                x, y = map(int, input("Nhập x, y (vd: 3,4): ").split(","))
                print(f"{x} x {y} = {product(x, y)}")

            case "4":
                n = int(input("Nhập n: "))
                result = "LÀ" if is_multiple_13_or_19(n) else "KHÔNG LÀ"
                print(f"{n} {result} bội số của 13 hoặc 19.")

            case "5":
                r = float(input("Nhập bán kính r: "))
                print(f"Diện tích hình tròn (r={r}) = {circle_area(r):.4f}")

            case "6":
                d, r = map(float, input("Nhập chiều dài, chiều rộng (vd: 5,3): ").split(","))
                print(f"Chu vi hình chữ nhật ({d} x {r}) = {rectangle_perimeter(d, r):.4f}")

            case "7":
                n = int(input("Nhập n: "))
                result = "LÀ" if is_perfect_square(n) else "KHÔNG LÀ"
                print(f"{n} {result} số chính phương.")

            case "8":
                n = int(input("Nhập n: "))
                result = "LÀ" if is_prime(n) else "KHÔNG LÀ"
                print(f"{n} {result} số nguyên tố.")

            case "9":
                a, b, c = map(int, input("Nhập 3 cạnh a, b, c (vd: 3,4,5): ").split(","))
                print(classify_triangle(a, b, c))

            case "0":
                print("Tạm biệt!")
                break

            case _:
                print("Lựa chọn không hợp lệ, vui lòng thử lại.")


menu()