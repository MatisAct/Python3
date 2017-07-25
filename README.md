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

- hàm `f.strip()` loại bỏ khoẳng trắng đầu cuối

- hàm `lower` chuyển thường , `upper()` hoa	, `swapcase()` swap hoa thường 

- hàm `file.find('ki tự tìm')` tìm kiếm 

- hàm replace('kí tự muốn đổi', 'kí tự cần đổi')

### kiểu dict :**quan ngại**

```
data={100:'Hoang' ,101:'Nam' ,102:'Binh'}
print data 
>>>{100: 'Hoang', 101: 'Nam', 102: 'Binh'}

-------------------------------------------
truy xuất parameter:
-------------------------------------------
dict = {'Ten': 'Hoang', 'Tuoi': 7, 'Ten': 'Nam'};

print "dict['Ten']: ", dict['Ten']
>>>dict['Ten']:  Nam
-----------------------------------------------
data1={'Id':100, 'Ten':'Thanh', 'Nghenghiep':'Developer'}
data2={'Id':101, 'Ten':'Chinh', 'Nghenghiep':'Trainer'}
print "Id cua nhan vien dau tien la",data1['Id']
print "Id cua nhan vien thu hai la",data2['Id']
print "Ten cua nhan vien dau tien la:",data1['Ten']
print "Nghe nghiep cua nhan vien thu hai la:",data2['Nghenghiep']
Kết quả là:
>>>>
Id cua nhan vien dau tien la 100
Id cua nhan vien thu hai la 101
Ten cua nhan vien dau tien la is Thanh
Nghe nghiep cua nhan vien thu hai la Trainer
---------------------------------------------
```
- Xóa phần tử từ Dictionary trong Python: `del ten_dictionary[key]`

|STT	|parameter|function|
|-------|---------|--------|
|1|Hàm cmp(dict1, dict2) |So sánh các phần tử của cả hai dict|
|2	|Hàm len(dict)|Độ dài của dict. Nó sẽ là số item trong Dictionary này|
|3|	Hàm str(dict)|Tạo ra một biểu diễn chuỗi có thể in được của một dict|
|4	|Hàm type(variable)|Trả về kiểu của biến đã truyền. Nếu biến đã truyền là Dictionary, thì nó sẽ trả về một kiểu Dictionary|
|5|	Phương thức dict.clear()|Xóa tất cả phần tử của dict|
|6	|Phương thức dict.copy()|Trả về bản sao của dict|
|7|	Phương thức fromkeys(seq,value1)/ fromkeys(seq)|Được sử dụng để tạo một Dictionary mới từ dãy seq và value1. Trong đó dãy seq tạo nên các key và tất cả các key chia sẻ các giá trị từ value1. Trong trường hợp value1 không được cung cấp thì value của các key được thiết lập là None|
|8|	Phương thức dict.get(key, default=None)|Trả về giá trị của key đã cho. Nếu key không có mặt thì phương thức này trả về None|
|9|	Phương thức dict.has_key(key)|Trả về true nếu key là có mặt trong Dictionary, nếu không là false|
|10|Phương thức dict.items()|Trả về tất cả các cặp (key-value) của một Dictionary|
|11|Phương thức dict.keys()|Trả về tất cả các key của một Dictionary|
|12|Phương thức dict.setdefault(key, default=None)|Tương tự get(), nhưng sẽ thiết lập dict[key]=default nếu key là không tồn tại trong dict|
|13|	Phương thức dict.update(dict2)|Được sử dụng để thêm các item của dictionary 2 vào Dictionary đầu tiên|
14|Phương thức dict.values()|Trả về tất cả các value của một Dictionary|

if __name__=='__main__':	

- kiểu kiểu như là hàm này để bắt đầu trương trình trong python , trong c thì int main() gì gì ấy 	Thì khi ta viết if __name__ == '__main__': thì Python sẽ thực thi phần lệnh phía sau của lệnh if nếu file này được thực thi bằng lệnh python. Đây là một phong cách lập trình của Python mà ta nên sử dụng.

### Day and time in python 

```
import time;

localtime = time.asctime( time.localtime(time.time()) )
>>>Thoi gian da duoc dinh dang la : Sun Nov 29 19:16:30 2015
```

- im ra calender:
```
import calender

calendar.month(2014, 6)


>>>
  November 2015
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30
```
# Hướng đối tượng trong  python

### Hướng thủ tục (Procedural-oriented)

Hướng thủ tục biểu hiện ở việc sử dụng các hàm trong Python. Bạn có thể định nghĩa các hàm, và các hàm này có thể sử dụng tại các module khác trong chương trình Python. hình như là cái hàm import ấy

### Hướng đối tượng (Object Oriented)

Hướng đối tượng trong **Python** biểu hiện ở việc sử dụng lớp (class), bạn có thể định nghĩa một class, class là một nguyên mẫu (prototype) để tạo ra các đối tượng (object/instance).

- tạo 1 class trong python: class lớn hơn function 
```
class ClassName:
   'Mô tả ngắn về class (Không bắt buộc)'
   # Code ...
```

- **Phương thức khởi tạo (Constructor):**


- Phương thức khởi tạo (Constructor) là một phương thức đặc biệt của lớp (class), nó luôn có tên là __init__

- Tham số đầu tiên của constructor luôn là self (Một từ khóa ám chỉ chính class đó).

- Constructor được sử dụng để tạo ra một đối tượng.

- Constructor gán các giá trị từ tham số vào các thuộc tính của đối tượng sẽ được tạo ra.

- Bạn chỉ có thể định nghĩa nhiều nhất một phương thức khởi tạo (constructor) trong class.

- Nếu class không được định nghĩa constructor, Python mặc định coi rằng nó thừa kết từ constructor của lớp cha.

vd: 
```
#	rectangle.py

# Class mô phỏng một hình chữ nhật.
class Rectangle :# khai báo tên class
	'''This is Rectangle class'''
	def __init__(self, width, height): #cái củ chuối này luôn phải có 

		self.width= width # chắc kiểu kiểu lấy giá trị vô cho self cái đoạn này méo hiểu thiệt @@
		self.height = height
	
	def getWidth(self): # function getwidth trả về giá trị của self,width
		return self.width
	def getHeight(self):
		return self.height
	def getArea(self):
		return self.width * self.height
      
 ------------------------------------------
 from rectangle import Rectangle # lấy từ module rectangle và class Redtangle
 
  
# Tạo 2 đối tượng: r1 & r2
 
from rectangle import Rectangle

r1 = Rectangle(10,5)

r2 = Rectangle(20,11)
print ("r1.width = ", r1.width)
print ("r1.height = ", r1.height)
print ("r1.getWidth() = ", r1.getWidth())
print ("r1.getArea() = ", r1.getArea())
print ("-----------------")
print ("r2.width = ", r2.width)
print ("r2.height = ", r2.height)
print ("r2.getWidth() = ", r2.getWidth())
print ("r2.getArea() = ", r2.getArea())

```
- kết quả :<img src="http://o7planning.org/vi/11415/cache/images/i/7508704.png">

- mô tả 2 cái trên : lúc này rectange truyền cho 2 cái r1 và r2  

<img src="http://o7planning.org/vi/11415/cache/images/i/7508535.png">

- cách truyền biến vô : 

<img src="http://o7planning.org/vi/11415/cache/images/i/7509015.png">

- python có thể cho chèn thêm 1 biến mới cho đối tượng có trước 

<img src="http://o7planning.org/vi/11415/cache/images/i/7523373.png">

- sau khi truyền 1 biến player1.adddresss=usa

<img src="http://o7planning.org/vi/11415/cache/images/i/7524101.png">

## Regular Expression trong Python

-  đại loại nó hoạt động để tạo ra sự khác biệt
```
- vd: print("ahihi\nahihi")
>>> ahihi
		ahihi
- còn khi sử dụng re:
vd:print(r"ahihi\nahihi")
>>> ahihi\nahihi

- nó giúp in ra các kí tự đặc biệt mà khỏi mất thời gian

```
- hoặc ví dụ 1 đoạn văn bản dài cả ngàn trang , có thể tìm kiếm các kí tự cụ thể , các số ...
```
import re
dich=open ('alphabet.txt','r').read()
print ("".join(re.findall(r"\d", dich))) # tìm các kí tự là số trong file
print ("".join(re.findall("[A-Za-z]", dich))) #tìm kí tự là string trong file 	
print ("".join(re.findall(r"[A-Za-z]{9,16}", dich))) #tìm kí tự dài từ 9-16,\w kí tự bất kì cặp số {số kí tự ít nhất, kết thúc}
print ("".join(re.findall(r"[A-Z]\w{1,}\s", dich))) #tìm kí tự là string trong file bắt đầu bằng từ in hoa,\s là kết thúc = space
```

- now , làm sao để có được statement trên: + re.findall để thêm 1 điều kiện , vd, nháy đơn hoặc nháy kép
<img src="https://image.prntscr.com/image/ciOT8Pj9SRKthq3U4ILuEQ.png">

|statement|cách dùng|
|---------|---------|
|\d|tim các kí hiệu số|
|{bắt đầu mấy kí tự, end}|việc tìm kiếm bn kí tự|
|\w |tìm các character|
https://www.youtube.com/watch?v=-p4U1jzqfhU&t=528s

- .*? lấy tất cả , vd ` re.findall(r'<title>(.*?)</title>') >>> lấy tất cả trong cụm title
