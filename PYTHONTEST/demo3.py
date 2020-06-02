

db = [
        {"username":"张三","password":"123456"},
        {"username":"李四","password":"123456789"}
    ]

zh = input("请输入账号:")
mm = input("请输入密码:")

for i in db:
    print("=======================")
    if zh == i.get("username") and mm == i.get("password"):
        print("输入的账号{}登录成功".format(zh))
    else:
        print("登陆失败！")    