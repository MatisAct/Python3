database={
	'statement':'cau lenh',
	'instruction':'chi dan',
	'parameter':'thong so',

}

def menu():
	print("==========================")
	print("==== hoc tieng anh nao====")
	print("==========================")
	print("1:them tu")
	print("2:tim tu")
	print("3:hien thi ra toan bo tu")
	print("nhan 0 de thoat ")
	print("==========================")
def themtu():
	word=input(">tu muon them:")
	mean=input(">nghia la:")
	database[word]=mean
	print("them thanh cong")

def timtu():
  word=input("+ ban muon tim tu nao:")
  if word in database:
    print('+tim thay-->%s :%s' %(word,database[word]))
  
  elif word=='thoat':
    print("thoat chuong trinh")
    exit(1)
  else:
    print("khong thay tu nay:")
  
def hienthi():
	for word,mean in database.items():
		print("%s:%s"%(word,mean))
		
menu()
luachon=int(input('>ban muon lam gi:'))
while luachon!=0:

	if luachon==0:
		break
		
	elif luachon==1:
	  themtu()
	  luachon=int(input('>ban muon lam gi:'))
	elif luachon==2:
		timtu()
		luachon=int(input('>ban muon lam gi:'))
	elif luachon==3:
		hienthi()
		luachon=int(input('>ban muon lam gi:'))
	
	else:
		print("yeu cau khong ton tai:")
		luachon=int(input('>ban muon lam gi:'))

