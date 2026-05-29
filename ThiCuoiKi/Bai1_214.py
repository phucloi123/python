#bai1_De214
lenght = float(input("Nhap chieu dai day hinh kho chu nhat(cm): "))
width = float(input("Nhap chieu rong day hinh kho chu nhat(cm): "))
height = float(input("Nhap chieu cao day hinh kho chu nhat(cm): "))
decimal_places = int(input("So luong so le can hien thi: "))

#tinh dien tich day chu nat
base_area = lenght * width

#tinh the tich hinh khoi
volume = lenght * width * height

#in ket qua ra
print(f"Dien tich day hinh chu nhat = {base_area:.{decimal_places}f} cm\u00b2")
print(f"The tich hinh khoi= {volume:.{decimal_places}f} cm\u00b3")