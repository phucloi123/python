from datetime import datetime, timedelta

# i) Thông tin thời gian hiện tại
now = datetime.now()

print("=== BÀI i ===")
print("Năm hiện tại:", now.year)
print("Tháng hiện tại (chữ):", now.strftime("%B"))
print("Tuần thứ trong năm:", now.isocalendar()[1])
print("Tuần thứ trong tháng:", (now.day - 1) // 7 + 1)
print("Ngày thứ trong năm:", now.timetuple().tm_yday)
print("Ngày hiện tại:", now.day)
print("Thứ của ngày:", now.strftime("%A"))
print("Giờ phút giây:", now.strftime("%H:%M:%S"))

# ii) Tính số ngày giữa 2 ngày
print("\n=== BÀI ii ===")
print("Nhập ngày thứ nhất:")
d1 = int(input("Ngày: "))
m1 = int(input("Tháng: "))
y1 = int(input("Năm: "))

print("Nhập ngày thứ hai:")
d2 = int(input("Ngày: "))
m2 = int(input("Tháng: "))
y2 = int(input("Năm: "))

date1 = datetime(y1, m1, d1)
date2 = datetime(y2, m2, d2)

diff = abs((date2 - date1).days)
print("Số ngày cách nhau:", diff)

# iii) Chuyển chuỗi sang datetime
print("\n=== BÀI iii ===")
s = input("Nhập chuỗi ngày (vd: Sep 18 2019 2:43PM): ")

dt = datetime.strptime(s, "%b %d %Y %I:%M%p")
print("Dạng datetime:", dt)

# iv) Cộng thêm 5 giây
print("\n=== BÀI iv ===")
future = now + timedelta(seconds=5)
print("Thời gian sau 5 giây:", future.strftime("%H:%M:%S"))