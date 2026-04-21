#bai 6
s = input("Nhap chuoi S: ")
work = input("Nhap tu can dem: ")

#Chuan hoa ve chu thuong de dem
s = s.lower()
work = work.lower()

#tach tu
works = s.split()

count = 0
for w in s:
    if w.strip(".,") == work:
        count += 1

print(f"So tu '{work}' la {count}")

#bai 13
import re
def chuan_hoa_chuoi(s):
# Xoa Khoang trang dau cuoi
    s = s.strip()

    return s

#Nhap
text = """   Quê hương   là  chùm khế  ngọt .
   Cho con trèo hái mỗi ngày .   """
print(chuan_hoa_chuoi(s))
