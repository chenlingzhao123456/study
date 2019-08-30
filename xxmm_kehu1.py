from tkinter import *
from socket import *
from threading import Thread
import time


win = Tk()
win.title('客户端')    #设置标题
win.geometry('330x440') #设置窗口大小
canvas =Canvas(master=win, width=330,height=440,bg='LightYellow')#创建画布设置背景色
canvas.pack()

client_info=None         #空值 储存客户端的信息

def get_info():
    while 1:
        buf_size = 1024     #服务端缓冲区的大小
        data=client_info.recv(buf_size)      #接收服务器发来的信息
        text.insert(INSERT,data.decode('utf8'))     #把收到的信息解码 然后显示在信息框上

def connect_server():
    global client_info
    ip=entry_ip.get()       #获取数据
    port=entry_port.get()
    user=entry_user.get()
    server_socket=socket(AF_INET, SOCK_STREAM) #创建socket对象
    address = (ip, int(port))   #封装地址
    server_socket.connect(address)      #连接服务器(ip和端口号)
    server_socket.send(user.encode('utf8'))    #把获取到的消息编码发送给客户端
    client_info=server_socket
    if __name__=='__main__':
        t=Thread(target=get_info)   #开启线程(任务)
        t.start()

def send_message(): #发消息
    send_who=entry_send_who.get()   #获取 发给谁 框里的内容
    send_msg=text_send.get('0.0','end') #获取要发的消息  就是显示消息 框里的内容(索引 浮点型)
    send_msg=send_who+':'+send_msg  #把消息重新赋值 格式 (谁:消息)
    client_info.send(send_msg.encode('utf8'))  #编码发送
    text_send.delete('0.0','end')

label_user = Label(master=win, text='用户名',bg='Lightpink')
label_user.place(x=20, y=20)
entry_user = Entry(master=win)
entry_user.place(x=70, y=20)
label_ip=Label(master=win,text='ip',bg='Lightpink')
label_ip.place(x=20,y=50)
entry_ip=Entry(master=win)
entry_ip.place(x=70,y=50)
label_port=Label(master=win,text='port',bg='Lightpink')
label_port.place(x=20,y=80)
entry_port=Entry(master=win)
entry_port.place(x=70,y=80)
button=Button(master=win,text='启动',bg='LightSkyBlue',height=1,width=40,command=connect_server)  #触发一个事件
button.place(x=20,y=110)

text=Text(master=win,height=5,width=30)
text.place(x=80,y=150)
label_text=Label(master=win,text='显示消息',bg='Lightpink')
label_text.place(x=20,y=170)

label_send=Label(master=win,text='发送消息',bg='Lightpink')
label_send.place(x=20,y=250)
text_send=Text(master=win,height=3,width=30)
text_send.place(x=80,y=240)

label_send_who=Label(master=win,text='发给谁',bg='Lightpink')
label_send_who.place(x=20,y=300)
entry_send_who=Entry(master=win)
entry_send_who.place(x=80,y=300)

button1=Button(master=win,text='发送',bg='LightSkyBlue',height=1,width=40,command=send_message)   #触发事件
button1.place(x=20,y=340)

win.mainloop()
