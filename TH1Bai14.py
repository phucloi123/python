# Chương trình đổi tiền tối ưu (số tờ ít nhất)

def doi_tien(x):
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    ket_qua = {}

    for tien in menh_gia:
        so_to = x // tien
        if so_to > 0:
            ket_qua[tien] = so_to
            x %= tien

    return ket_qua

def main():
    print("=" * 40)
    print("   CHUONG TRINH DOI TIEN TOI UU")
    print("=" * 40)

    while True:
        try:
            x = int(input("\nNhap so tien X: "))
            if x <= 0:
                print("Vui long nhap so tien lon hon 0!")
                continue
            break
        except ValueError:
            print("Vui long nhap so nguyen hop le!")

    ket_qua = doi_tien(x)

    print("\n" + "=" * 40)
    print(f"  So tien can doi: {x:,}")
    print("=" * 40)
    print(f"  {'Menh gia':<15} {'So to':>10}")
    print("-" * 40)

    tong_to = 0
    for menh_gia, so_to in ket_qua.items():
        print(f"  {menh_gia:<15,} {so_to:>10}")
        tong_to += so_to

    print("=" * 40)
    print(f"  Tong so to: {tong_to}")
    print("=" * 40)

main()