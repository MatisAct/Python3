# Lập trình Socket
invalid syntax book
### Lập trình socket là gì ?
- Lập trình socket là cách lập trình cho phép chúng ta kết nối các máy tính truyền tải và nhận dữ liệu từ máy tính thông qua mạng .
### Có 2 loại socket gồm : TCP/UDP
- **TCP**: có hướng kết nối
- **UDP**:không có hướng kết nối
#### 1/ Giới thiệu về socket
Socket là một giao diện lập ứng dụng mạng . Thông qua giao diện này, chúng ta có thể lập trình điều khiển, truyền thông giữa 2 máy sử dụng giao thức TCPIP và UDP.
Socket là thiết bị truyền thông hai chiều gửi và nhận dữ liệu từ máy khác
+ Các loại socket
►Socket có hướng kết nối (TCP):
►Socket không hướng kết nối (UDP)
**Đặc điểm của socket hướng kết nối**
+ Có một đường kết nối (địa chỉ IP) giữa 2 tiến trình
+ Một trong 2 tiến trình kia phải đợi tiến trình kia yêu cầu kết nối.
+ Có thể dùng để liên lạc theo mô hình client và sever
+ Mô hình client /sever thì sever lắng nghe và chấp nhận từ client
+ Mỗi thông điệp gửi phải có xác nhận trả về
+ Các gói tin chuyển đi tuần tự.
**Đặc điểm socket không hướng kết nối:**
+ 2 Tiến trình liên lạc với nhau không kết nối trực tiếp
+ Thông điệp gửi đi phải kèm theo thông điệp người nhận
+ Thông điệp có thể gửi nhiều lần 
+ Người gửi không chắc chắn thông điệp đến tay người nhận.
+ Thông điệp gửi sau có thể đến trước và ngược lại.
Số hiệu cổng của Socket

Để có thể thực hiện các cuộc giao tiếp , một trong 2 quá trình phải công bố số hiệu cổng của socket mà mình đang sử dụng
Mỗi công giao tiếp phải thể hiện một địa chỉ xác định trong hệ thống.
Khi quá trình được gán một số hiệu cổng , nó có thể nhận dữ liệu gửi đến chỗ này từ quá trình khác
### 2/ Khái niệm về địa chỉ và cổng (Address ,Port )
Khi cần trao đổi dữ liệu cho nhau thì 2 ứng dụng cần phải biết thông tin tối thiểu là IP và sô hiểu cổng của ứng dụng kia.
+ 2 ứng dụng có thể nằm cùng trên một máy
+ 2 ứng dụng cùng nằm trên một máy không được cùng số hiệu cổng

Thiết lập giao tiếp

<h3>Để dễ hiểu hơn! Chúng ta quay trở lại với chiếc điện thoại.</h3>

#### Đầu tiên muốn gọi-nghe từ điện thoại của ai đó. Bạn phải có 1 chiếc điện thoại.
Điều này đồng nghĩa là :

#### Mua mới 1 chiếc điện thoại Nó là việc bạn tạo 1 socket để chú ý lắng nghe các connections. Method socket() sẽ làm việc này. Vậy có nhiều người cùng có điện thoại. Vậy làm sao để biết được bạn sẽ gọi cho ai?
+ Bạn cần 1 địa chỉ liên lạc riêng biệt .Như vậy bạn cần đánh địa chỉ cho socket của mình. Method bind() sẽ làm tốt việc này. Thường thì chúng ta sử dụng 2 loại:

- AF_UNIX : UNIX pathnames
- AF_INET : Internet address : Sử dụng các số 4 bytes . Ví dụ : 192.168.1.1 Và chúng ta có thường dùng 2 loại socket. Có 2 option sau để 

phân biệt:

SOCK_STREAM

SOCK_DGRAM

Tương ứng với Stream Sockets và Datagram Sockets. Đôi lúc gọi datagram sockets là “Connectionless sockets”. Stream Socket có 2 cách 

thiếp lập giao tiếp stream.

Nếu output của bạn là 2 item đến socket theo thứ tự là “1,2” , chúng sẽ nhận theo thứ tự “1,2”. 

Cái gì sử dụng stream sockets? Có nhiều tool và điển hình browser get 1 trang web. Cây html bạn nhận được sẽ đúng theo thứ tự nó được 

trình bày. 

OK. Chúng ta tiếp tục với tình huống : Nhiều người cùng gọi vào số 1 số điện thoại.

Bạn đưa các cuộc gọi cùng lúc vào danh sách đợi.

Method listen() làm tốt việc này. Nó thiết lập số maximum các request ( thường là 5).

Khi cuộc gọi tới bạn chấp nhận nó. Điện thoại đổ chuông.

Method accept() làm việc chấp nhận request, thành lập 1 connection. Tuy nhiên, bạn có thể accept khi đang xử lý 1 process trước đó. 

Tới đây bạn đang nhận 1 các cuộc gọi tới.

Gọi đi

Cách để call 1 socket là dùng method connect(). Vậy làm sao để gọi cho nửa kia. Bạn phải có số điện thoại người ấy. Như vậy bạn phải có 

1 địa chỉ socket đang ready. Sẵn sàng lắng nghe các cuộc gọi đến.

Trao đổi

Và giờ bạn đã có 1 connection giữa socket, bạn muốn send data giữa chúng. 

Hàm send() và recv() được sử dụng ở đây… Cuộc nói chuyện tiếp diễn…

Kết thúc

Cuộc nói chuyện nào cũng có hồi kết.

Hàm close() được sử dụng ở đây.



hey i need you read PythonNetBinder !now  

```
server.py 
<-------------->
import socket
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

/*Đầu tiên chúng ta tạo một đối tượng socket, tham số AF_INET cho biết chúng ta sử dụng IP v4, SOCK_TREAM là dùng giao thức TCP. Ngoài ra còn một số giá trị khác như AF_INET6 là dùng IP v6, AF_UNIX là chỉ kết nối các ứng dụng trong một máy (không dùng mạng), SOCK_DGRAM là dùng giao thức UDP.*/

print ("Starting server on port 10000")
server.bind((socket.gethostname(), 10000))
#Phương thức bind() liên kết tới địa chỉ gethostname() trên cổng 10000.
server.listen(1)
Phương thức listen() cho python biết socket này là một server, tham số của phương thức này là số lượng các kết nối có thể có trong hàng đợi, ít nhất là 0 và cao nhất là do hệ điều hành chỉ định (thường là 5). Phương thức accept() sẽ đưa server vào trạng thái chờ đợi cho đến khi có kết nối thì sẽ trả về một tuple gồm có một socket khác dùng để truyền dữ liệu qua lại với client và một tuple nữa bao gồm địa chỉ ip và port của ứng dụng client.

while True:
    conn, client = server.accept()
    try:
       print ("Connection from", client)
  
    while True:
        data = conn.recv(1024)
        print ("Receive from client:", data)
        if data:
            print ("Response to client")
            conn.sendall(data) #ếu có dữ liệu gửi sang thì chúng ta gửi trả lời về client thông qua phương thức sendall()
        else:
            print ("No data received")
            break
    finally:
        conn.close()
```


• send() returns actual bytes sent
• recv() length is only a maximum limit

>>> s.setsockopt(socket.SOL_SOCKET,
... socket.SO_REUSEADDR, 1)
>>> s.bind(("",9000))
