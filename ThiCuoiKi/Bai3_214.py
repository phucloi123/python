# Bai3_214.py - Lambda functions
import math

# Ham lambda kiem tra so chinh phuong (perfect square)
# Cat phan thap phan cua sqrt(n) roi binh phuong lai, neu bang n thi la so chinh phuong
is_perfect_square = lambda n: int(math.sqrt(n)) ** 2 == n

# Ham lambda kiem tra 3 canh co hop le khong
# Dieu kien tam giac: tong 2 canh bat ky phai lon hon canh con lai
is_valid_triangle = lambda a, b, c: a + b > c and a + c > b and b + c > a

# Ham lambda kiem tra tam giac vuong theo dinh ly Pythagoras
# Sap xep tang dan, canh lon nhat [2] la can huyen
is_right_triangle = lambda a, b, c: sorted([a, b, c])[2] ** 2 == sorted([a, b, c])[0] ** 2 + sorted([a, b, c])[1] ** 2

# Phan loai tam giac - dinh nghia TRUOC khi goi
def classify_triangle(a, b, c):
    # Kiem tra 3 canh co tao thanh tam giac hop le khong
    if not is_valid_triangle(a, b, c):
        return "Khong phai tam giac hop le"

    # Phan loai theo do dai canh
    if a == b == c:
        return "Tam giac deu"       # 3 canh bang nhau
    elif a == b or b == c or a == c:
        return "Tam giac can"       # 2 canh bang nhau
    elif is_right_triangle(a, b, c):
        return "Tam giac vuong"     # co goc 90 do
    else:
        return "Tam giac thuong"    # khong co tinh chat dac biet

# ---- Chuong trinh chinh ----

# Phan 1: Kiem tra so chinh phuong
n = int(input("Nhap so nguyen n: >? "))
print(f"{n} {'la' if is_perfect_square(n) else 'khong la'} so chinh phuong")

# Phan 2: Phan loai tam giac
# Ho tro ca 2 cach nhap: "2 3 5" hoac "2,3,5"
raw = input("Nhap 3 canh tam giac (a b c): >? ")
a, b, c = map(int, raw.replace(',', ' ').split())
print(classify_triangle(a, b, c))