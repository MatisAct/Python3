print("==============================")
print("=====chuong trinh tinh lai====")
print("==============================")

lai=float(input(">nhap lai xuat:"))

tien=float(input(">so tien gui vao:"))
thang=int(input(">so thang gui:"))
tong=tien
for a in range(thang):
	tong=tong +tong*(lai/100)
print("so tien nhan duoc sau",thang, "thang la",tong)
