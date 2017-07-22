# Lập trình Socket

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
