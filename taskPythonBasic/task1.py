# Viết chương trình nhập vào năm sinh, in ra tuổi, ví dụ nhập 1984 in ra: Ban sinh năm 1984, vay ban 19 tuoi.
namsinh=int(input(">Nhap nam sinh cua ban:"))
namhientai=int(input(">nhap nam hien tai:"))
tuoi=namhientai-namsinh
if tuoi<0:
	print("ban nhap sai nam sinh")
elif tuoi==0:
	print("ban duoc 1 tuoi roi ahihi")
else:
	print("tuoi hien tai cua ban la:",tuoi)
