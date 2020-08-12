_usrname=input("请初始化用户名:")
_password=input("请初始化登录密码:")

print (_usrname)
print (_password)

flag0=0
flag1=0
print("----------用户登录----------")

while True:
    user=input("请输入用户名:")
    if user==_usrname:
        print("用户名输入正确")
        while flag0<3:
            password=input("请输入密码:")
            if password==_password:
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
