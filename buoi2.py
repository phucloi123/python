dai = float(input("Nhập chiều dài đáy hình chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
so_le = int(input("Số lượng số lẻ cần hiển thị: "))

# Tính toándien_tich_day = dai * rong
the_tich = dien_tich_day * cao

# Xuất kết quả đã làm tròn
print(f"Diện tích đáy hình chữ nhật = {round(dien_tich_day, so_le)}cm²")
print(f"Thể tích hình khối = {round(the_tich, so_le)}cm³")
# Nhập 3 số nguyên
a = int(input("Nhập số thứ nhất a: "))
b = int(input("Nhập số thứ hai b: "))
c = int(input("Nhập số thứ ba c: "))

# Tìm số nhỏ nhất và lớn nhất
so_nho = min(a, b, c)
so_lon = max(a, b, c)
# Tìm số ở giữa bằng cách lấy tổng trừ đi hai số kia
so_giua = (a + b + c) - so_nho - so_lon

# Xuất kết quả dùng phương thức format
ket_qua = "Thứ tự tăng dần: {} {} {}".format(so_nho, so_giua, so_lon)
print(ket_qua)
# Nhập số nguyên dương a (1-9)
a_str = input("Nhập số nguyên dương a (1-9): ")

# Tạo các giá trị aa và aaa bằng cách nhân chuỗi
aa_str = a_str * 2    # Ví dụ '5' * 2 = '55'
aaa_str = a_str * 3   # Ví dụ '5' * 3 = '555'

# Chuyển về số nguyên và tính tổng
a = int(a_str)
aa = int(aa_str)
aaa = int(aaa_str)
tong = a + aa + aaa

# In kết quả theo định dạng ví dụ
print(f"{a} + {aa} + {aaa} = {tong}")