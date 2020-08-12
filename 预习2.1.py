Usrname=input("请初始化用户名:")
Password=input("请初始化登录密码:")

print (Usrname)
print (Password)
#flag0为密码输入错误次数
#flag1为用户名和密码全部输入成功的标志
flag0=0
flag1=0
print("----------用户登录----------")

while True:
    user=input("请输入用户名:")
    if user==Usrname:
        print("用户名输入正确")
        while flag0<3:
            password=input("请输入密码:")
            if password==Password:
                print("----------登录成功----------")
                flag1=1
                break
            else: 
                flag0 +=1
                if flag0<=2:
                   print("密码错误，请重新输入！")
        if flag1==1:
             break
        flag0=0
        flag1=0
        print ("您已输入错误三次，请重新登陆")
    else:
        print ("用户名不存在，请重新输入！")
