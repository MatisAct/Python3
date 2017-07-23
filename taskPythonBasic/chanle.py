
print("=======================================")
print("| chuong trinh kiem tra chan le cua so|")
print("=======================================")

so=int(input(">nhap so can kiem tra:"))

if so%2==0:
	print("so ban nhap la so chan")
else:
	print("so ban vua nhap la so le")
b=list(range(0,so))
print("day so truoc so ban nhap:",b)

print("cac so chan la:")
for i in range(0,so):
	if i%2==0:
		print (i,end=' ')

