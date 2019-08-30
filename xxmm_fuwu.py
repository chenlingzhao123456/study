from tkinter import *
from socket import *
from threading import Thread
import time


win = Tk()
win.title('服务端')    #设置标题
win.geometry('300x260') #设置窗口大小
canvas =Canvas(master=win, width=300,height=260,bg='LightYellow') #创建画布 设置窗口背景色
canvas.pack()
users = {}      #存客户端信息(用户名 ip port)


def run(client_socket):
    buf_size = 1024 #服务端缓冲区的大小
    data = client_socket.recv(buf_size)  # 服务端接收数据
    message_recv=data.decode('utf8')    #数据解码
    # print(message_recv)   #打印结果是 用户名
    users[message_recv] = client_socket  # 解码保存信息到字典 user={用户名:客户端消息(ip,port)}
    text.insert(INSERT,message_recv + '已连接\n')    #在消息框显示是否连接成功
    while 1:
        data1 = client_socket.recv(buf_size)   #接收客户端传来的消息
        data2 = data1.decode('utf8')  #data2打印出来样式  谁谁 : 消息内容
        info_list = data2.split(':')    #以 : 切分字符串,样式是['谁谁','消息内容']
        name=info_list[0]
        thetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        users[name].send(thetime.encode('utf8'))
        users[name].send(('\n'+message_recv + '说:' + info_list[1]).encode('utf8'))   #把收到的 消息内容 发送出去( 用户名+ 说: 消息内容)

def start():
    ip = entry_ip.get()  # 获取ip
    port = entry_port.get()  # 获取端口
    address = (ip, int(port))   #封装地址
    server_socket = socket(AF_INET, SOCK_STREAM)    #创建socket对象
    server_socket.bind(address)  # 绑定ip和端口号
    server_socket.listen(5)    #开启服务器监听
    text.insert(INSERT, '服务器启动成功\n')  # 连接消息窗口显示
    while 1:
        # 接收客户端的链接请求
        client_socket, client_address = server_socket.accept()  #阻塞 同步的
        # 开启一个线程(只要有客户端接入就会开启一个线程)
        if __name__=='__main__':
            t = Thread(target=run, args=(client_socket,))
            t.start()


def start_sever():
    t = Thread(target=start)  # 开启一个线程(任务是开启服务器)
    t.start()


label_ip = Label(master=win, text='ip',bg='Lightpink')
label_ip.place(x=20, y=20)
label_port = Label(master=win, text='port',bg='Lightpink')
label_port.place(x=20, y=50)
entry_ip = Entry(master=win)
entry_ip.place(x=60, y=20)
entry_port = Entry(master=win)
entry_port.place(x=60, y=50)
button = Button(master=win, text='启动',bg='LightSkyBlue', height=1, width=36,command=start_sever)       #触发事件
button.place(x=20, y=80)
text = Text(master=win, height=5, width=30)
text.place(x=60, y=130)
label_text = Label(master=win, text='连接消息',bg='Lightpink')
label_text.place(x=5, y=150)

win.mainloop()
