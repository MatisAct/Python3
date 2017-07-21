import socket
def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print "Host name: %s" % host_name
    print "IP address: %s" % ip_address
    
if __name__ == '__main__':
    print_machine_info()
#Về ý nghĩa của nó thì nó giống như các C và các ngôn ngữ khác bắt đầu một chương trình. Ta cần có một điểm để bắt đầu.
Thì khi ta viết if __name__ == '__main__': thì Python sẽ thực thi phần lệnh phía sau của lệnh if nếu file này được thực 
thi bằng lệnh python.Đây là một phong cách lập trình của Python mà ta nên sử dụng.
