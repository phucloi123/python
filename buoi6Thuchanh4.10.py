#bai 3
S = list(map(int, input('Nhap so dien thoai: ').split()))

for x in S:
    if x not in (4, 6, 7):
        print(x,end=" ")

#bai 4
lst = input("Nhap Chuoi: ").split()
print(lst)
for x in lst:
    if lst.count(x) > 1:
        print('Chu đầu tiên trong là: ', x)
        break