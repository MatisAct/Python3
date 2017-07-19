## Python 3:

### **cú pháp cơ bản**


- print (bien can in,'câu cần in',end='so khoang trang can in',bien can in)
 - muốn truyền vào trong :print('in in in %s .%d'),%('dấu',số thì khỏi)

- hoặc truyền biến:
```
deptrai="ahihi"
tuoi=20
print("{} dep trai ahhhh {} tuoi".format(deptrai,tuoi))

>>>ahihi dep trai ahhhh 20 tuoi

```
dùng lệnh end để gom các lệnh print trên 1 hàng,vd print(end='mời bạn nhập 1 số')
```
print(end='Mời bạn nhập 1 số:')
a=input() ** int(nếu bạn nhập số  nguyên , thay dạng để nhập)
print('số bạn vừa nhập = ',a)
 
print('Mời bạn nhập 1 số',end=':')
b=input()
print('số bạn vừa nhập =',b)
```

- vòng lặp : lệnh contiue quay lại vòng lặp và bỏ qua câu lệnh sau nó
```
for biến in mảng( có thể là hàm range()):
	if điềuu kiện:
		câu lệnh
```

- lệnh if còn có thể: if biến in (các giá trị): đối với c là && ||


- chèn với lệnh insert:
 
 cú pháp: biến. insert(vị trí chèn,cái cần chèn)

- hàm : cú pháp

```
def tênhàm():
	"chú thích "
	biểu thức
	return


```

- một số cái sida cần biết:	

```
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2 **hàm trả về số lần suất hiện của keyword**
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3 **tìm coi keyword ở đâu,** 
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6 **như trên bắt đầu từ vị trí 4**
>>> fruits.reverse()
>>> fruits **đảo ngược lại**
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits **thêm keyword vào trong**
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits **sắp lại theo aphebet)
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
**loại bỏ phần tử cuối và hiển thị ra nó**
```

- ví dụ for:
```
vec = [-4, -2, 0, 2, 4]
x*2 for x in vec]
>>>[-8, -4, 0, 4, 8]
```

- lệnh del
```
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

- ví dụ:
```
from sys import argv # lấy tính năng argv từ thư viện system
script,first,second,third =argv
print('the script is called:',script)
print('your fisrst variable is:',first)
print('your second variable is:',second)
```

<img src="https://image.prntscr.com/image/PHa-9vWVSgyY3PnP-ajJGg.png">

- **thao tác với file** : tương tự như c vụ mở file , còn in file ra màn hình thì ` file.read()` , có thể gom thành 1 hàm vừa mở vừa đọc,`open('filename','r').read()` , lệnh `file.seek(0)` trả về vị ví ban đầu , nghia là đang ở cuối seek 1 cái về ngay vị trí 0 đầu file hàm `readline`

```
# hàm ghi file
from sys import argv 
script,filename=argv
print("we're going to erase %r",filename)
print("if bn don't want that, hit crt-c")
print("if you do want that, hit return")
input("?") # nếu bạn ấn crt+c chương trình tự hủy, ko thì nhấn phím khác
print("openning the file...")
targe=open(filename,'w') # mở file để ghi vô
print("truncating the file.Goobye")
targe.truncate() # làm trắng file
print("now 'am going ask you for three line ")
line1=input('line 1:') # nhập dô dòng 1
line2=input('line 2:')
line3=input('line 3:')
print("i'm going to write these to the file")
targe.write(line1) # in vô file
targe.write('\n')
targe.write(line2)
targe.write('\n')
targe.write(line3)
targe.write('\n')

print('and finally , we close it')
targe.close()
```

- **import** : sử dụng các thư viện của python , hoặc các code dạng tên(module).py để sử dụng cái này tự mình tạo, tích hợp nhiều code vs nhau

Nếu chúng ta muốn import module “urllib”, thư viện này dùng để đọc dữ liệu từ các URL, thì chúng ta sử dụng từ khóa import như sau:
```
# import the library
import urllib

# use it
urllib.urlopen("http://vnexpress.net/")// ví dụ 1 function tên là deff, khi sử dụng , urllib.deff(paramater(thông số))
```

- **cú pháp from tên import** :http://vietjack.com/python/module_trong_python.jsp

```
from module import *
Cú pháp trên có ý nghĩa là tích hợp tất cả những gì có trong module vào chương trình của chúng ta ngoại trừ các đối tượng có tên bắt đầu bằng dấu gạch dưới _. Những đối tượng này được sử dụng với tên của module chứ không thể được gọi riêng như những đối tượng khác.

-----1-----------
everything.py
from math import *
 
print (cos(3))
print (pi)
------------------
Output

-0.9899924966
3.14159265359

----hoặc----
import math

print(math.cos(90))
---
>1.0
---------3--------
import math as m
 
print (m.pi)
print (m.cos(3))
----------------
kết quả như vậy, vì hàm math truyền cho m rồi
```


- **thao tác vs chuooi~**
