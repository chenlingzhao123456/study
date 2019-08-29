stuinfolist = []


def showinfo():  # 显示功能列表
    print('欢迎进入学生管理系统 < Python版 >'.center(51))
    print('-' * 50)
    print('请选择你的操作:'.center(47))
    print('添加学生信息请按:1'.center(50))
    print('查询单个学生信息请按:2'.center(51))
    print('删除学生信息请按:3'.center(50))
    print('修改学生信息请按:4'.center(50))
    print('查询所有学生信息:5'.center(50))
    print('退出操作请按:6'.center(47))
    print('-' * 50)


def addinfo(name, gender, age, student_number):  # 添加学生信息
    stuinfo = {'name': name, 'gender': gender, 'age': age, 'student_number': student_number}

    stuinfolist.append(stuinfo)
    print('添加成功!')


def searchinfo(student_number):  # 查询单个信息
    for stuinfo in stuinfolist:
        if stuinfo.get('student_number') == student_number:
            return stuinfo
    return None


def delinfo(student_number):  # 删除信息)
    res = searchinfo(student_number)
    if res:
        stuinfolist.remove(res)
        print('删除成功!')
    else:
        print('查无此人!请重新输入!')


def modifyinfo(student_number):  # 修改信息
    res = searchinfo(student_number)
    if res:
        print(res)
        name = input('请输入修改后的学生姓名:')
        gender = input('请输入修改后的学生性别:')
        age = input('请输入修改后的学生年龄:')
        res['name'] = name
        res['gender'] = gender
        res['age'] = age
    else:
        print('查无此人!请重新输入!')


def enter():  # 登录
    while True:
        username = input('请输入用户名:')
        pwd = input('请输入密码:')
        if username == 'admin' and pwd == '123':
            print('登录成功!')
            break
        else:
            print('输入错误!请重新输入!')


def students_show():
    enter()
    showinfo()
    while True:
        num = input('请输入指令:')
        num = int(num)
        if num == 1:
            name = input('请输入要添加的学生姓名:')
            gender = input('请输入要添加的学生性别:')
            age = input('请输入要添加的学生年龄:')
            student_number = input('请输入要添加学生的学号:')
            student_number = int(student_number)
            addinfo(name, gender, age, student_number)

        elif num == 2:
            print('欢迎进入查询功能!')
            student_number = input('请输入要查询学生的学号:')
            student_number = int(student_number)
            res = searchinfo(student_number)
            if res:
                print(res)
            else:
                print('查无此人!请重新输入!')
        elif num == 3:
            student_number = input('请输入要删除的学生学号:')
            student_number = int(student_number)
            delinfo(student_number)
        elif num == 4:
            student_number = input('请输入要修改的学生学号:')
            student_number = int(student_number)
            modifyinfo(student_number)
        elif num == 5:
            print(stuinfolist)
        elif num == 6:
            print('退出操作')
            break
        else:
            print('操作错误!请输入1~6之间的整数!')


students_show()
