print("=============================")
print("|-phan mem kiem tra mat khau|")
print("=============================")

b=input(">Nhap mat khau:")

print("cac loi trong mat khau cua ban:")
if len(b)<7:
	print("mat khau yeu, qua it ki tu")
if b.isalpha()==True:
	print("mat khau cua ban phai co chu va so")
if b.islower()==True:
  print("mat khau phai can co chu in hoa")
  
for i in range(0,len(b)):
  if b[i]==" ":
    print("mat khau khong duoc co khoang trang")





