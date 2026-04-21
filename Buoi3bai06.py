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