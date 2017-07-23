k=0
b=int(input(">nhap so muon kiem tra:"))
if 0<b<3:
	print("so ban nhap la so nguyen to")
	exit()

	
for a in range(2,int(b/2)+1):
	if b%a==0:
		k=1
		break

if k==0:
  print("la so nguyen to")
else:
  print("ko la so nguyen to")

