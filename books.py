class Administrator:
    books = []

    def __init__(self, students=[]):
        self.students = students

    def addbook(self, bookname):    #添加图书
        self.books.append(bookname)
        print('添加成功!')

    def addstudent(self, studentnumber, age, name, bookname, borrowdate):   #添加学生借书信息
        student = {'studentnumber': studentnumber, 'age': age, 'name': name, 'bookname': bookname,
                   'borrowdate': borrowdate}
        self.students.append(student)

    def searchbook(self, bookname):     #查询图书
        if bookname in self.books:
            print(self.books)
        else:
            print('没有这本书! 请重新输入!')

    def searchstudent(self, studentnumber):     #查询学生借书信息
        for student in self.students:
            if student.get('studentnumber') == studentnumber:
                return student
            else:
                print('找不到信息! 请重新输入!')

    def lendbook(self, bookname):       #借出书
        if bookname in Administrator.books:
            self.books.remove(bookname)
            studentnumber = input('请输入你的学号:')
            age = input('请输入你的年龄:')
            name = input('请输入你的姓名:')
            borrowdate = input('请输入你的借书日期:')
            Administrator().addstudent(studentnumber, age, name, bookname, borrowdate)
            print('借书成功!')
        else:
            print('没有这本书! 请重新输入!')

    def receivebook(self, bookname):    #收到书
        self.books.append(bookname)
        print('还书成功!')

    @staticmethod
    def show():
        print('欢迎进入图书管理系统'.center(50))
        print('-' * 50)
        print('查询图书请按:1'.center(50))
        print('添加图书请按:2'.center(50))
        print('借阅图书请按:3'.center(50))
        print('归还图书请按:4'.center(50))
        print('退出系统请按:5'.center(50))
        print('-' * 50)

    @staticmethod
    def enter():
        while True:
            username = input('请输入用户名:')
            pwd = input('请输入密码:')
            if username == 'admin' and pwd == '123':
                print('登录成功!')
                break
            else:
                print('输入错误!请重新输入!')


class Main:
    def student_show(self):
        Administrator.enter()
        Administrator.show()
        while True:
            num = input('请输入指令:')
            num = int(num)
            if num == 1:
                bookname = input('请输入要查询的图书名:')
                Administrator().searchbook(bookname)
            elif num == 2:
                bookname = input('请输入要添加的图书名:')
                Administrator().addbook(bookname)
            elif num == 3:
                print(Administrator.books)
                bookname = input('请输入要借阅的图书名:')
                Administrator().lendbook(bookname)
            elif num == 4:
                studentnumber = input('请输入归还图书的学生学号:')
                res = Administrator().searchstudent(studentnumber)
                if res:
                    Administrator().students.remove(res)
                    Administrator().receivebook(res.get('bookname'))
                else:
                    print('没有这个人的借书信息!')
            elif num == 5:
                print('程序结束!')
                break
            else:
                print('操作错误!请输入1~6之间的整数!')

m=Main()
m.student_show()