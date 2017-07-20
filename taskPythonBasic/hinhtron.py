#chu vi dien tich hinh tron
import math
bankinh=float(input("nhap ban kinh:"))
if bankinh<0:
    print "Ban kinh khong nho hon 0"
    print "Ban nhap khong hop le"
else:
	CV=2*bankinh*math.pi
	DT=bankinh*bankinh*math.pi
	print "Chu vi la :",CV
	print "Dien tich la :",DT
