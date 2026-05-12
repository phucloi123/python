# Bai 20 + Mo rong: Doi tien toi uu + Thu ngan

def doi_tien(x):
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    ket_qua = {}
    for tien in menh_gia:
        so_to = x // tien
        if so_to > 0:
            ket_qua[tien] = so_to
            x %= tien
    return ket_qua

def in_ket_qua(so_tien, ket_qua):
    print(f"\nSo tien {so_tien} duoc doi thanh:")
    tong_to = 0
    so_loai = 0
    menh_gia_tat_ca = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    for mg in menh_gia_tat_ca:
        so_to = ket_qua.get(mg, 0)
        if so_to > 0:
            print(f"  Loai {mg} gom {so_to} to")
            tong_to += so_to
            so_loai += 1
    print(f"TONG CONG CO {tong_to} TO")
    print(f"Tong so loai = {so_loai}")

# ====== PHAN MO RONG: THU NGAN ======
print("=" * 45)
print("       CHUONG TRINH THU NGAN")
print("=" * 45)

while True:
    try:
        a = int(input("\nNhap so tien hang can phai tra (a): "))
        b = int(input("Nhap so tien khach dua (b):          "))
        if a <= 0 or b <= 0:
            print("Vui long nhap so tien lon hon 0!")
            continue
        break
    except ValueError:
        print("Vui long nhap so nguyen hop le!")

print("-" * 45)

if a > b:
    thieu = a - b
    print(f"\nKhach hang con thieu: {thieu}")
    print("Xin vui long thanh toan them. Tam biet!")

elif a == b:
    print("\nCam on khach hang. Hen gap lai!")

else:  # a < b
    tien_thua = b - a
    print(f"\nSo tien can tra lai cho khach: {tien_thua}")
    ket_qua = doi_tien(tien_thua)
    in_ket_qua(tien_thua, ket_qua)
    input("\nNhan Enter de ket thuc...")
    print("\nCam on khach hang. Hen gap lai!")