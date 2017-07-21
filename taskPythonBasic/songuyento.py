# thuật toán chưa tối ưu
k=0
b=int(input(">nhap so muon kiem tra:"))
if b==2:
	print("so ban nhap la so nguyen to")
	
for a in range(2,b):
	if b%a==0:
		k+=1
if k==0:
  print("la so nguyen to")
else:
  print("ko la so nguyen to")




 
			
