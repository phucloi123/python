#Viet chuong trinh Python su dung lambda đe tinh truong hop sau
# a
n = int(input('Nhap vao so nguyen duong: '))
f = lambda n: abs(n) #ham lambda, n la tham so dau vao, abs la gia tri tra ve
print('tri tuyet doi cua n la:', f(n))

#b
f = lambda n: n+15
print('gia tri tra ve la: ', f(n))

#c
x, y = map(int, input('nhap so nguyen (x, y): ').split()) # nhap 2 so nguyen
lamb = lambda x, y: x * y
print('tich cua 2 so (x va Y) la:', lamb(x, y))

#d
n = int(input('Nhap so nguyen n: '))
lamd = lambda n : n % 13 == 0 or n % 19 == 0# neu la boi cua 13 va 19 thi true , neu khong la false
print(f'{n} la boi cua so cua {lamd(n)}')

#e
r = float(input('Nhap ban kin cua hình tron: '))
lambA = lambda r: 3.14 * r * r # dien tich hinh tron la A=3.14*r^2
print('dien tich cua hinh tron la: ', lambA(r))

#f
d, r= map(float, input('Nhap chieu dai va chieu rong cua HCN: ').split())
lambCV = lambda d, r: 2 * ( d + r) # chu vi HCN la P = 2(d+r)
print('chu vi hinh chu nhat la: ', lambCV(d, r))

#g
n = int(input("nhap so nguyen duong: "))
lambG= lambda n : int(n**0.5)**2 == n
print(f'{n} So chinh phuong hay khong: ', lambG(n))

#h
n = int(input("nhap so nguyen duong: "))
lambH = lambda n: n > 1 and all(n % i != 0 for i in range(2, n))
print(f'{n} So nguyen to hay khong: ', lambH(n))

#i
a,b,c = map(int,input("Nhap a b c: ").split())

hop_le = lambda a,b,c: a+b>c and a+c>b and b+c>a

loai = lambda a,b,c: (
    "Tam giac deu" if a==b==c else
    "Tam giac vuong" if sorted([a,b,c])[0]**2 + sorted([a,b,c])[1]**2 == sorted([a,b,c])[2]**2 else
    "Tam giac can" if a==b or b==c or a==c else
    "Tam giac thuong"
)

if hop_le(a,b,c):
    print(loai(a,b,c))
else:
    print("Khong phai tam giac")