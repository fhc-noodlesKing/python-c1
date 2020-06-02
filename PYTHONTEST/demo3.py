

# db = [
#         {"username":"张三","password":"123456"},
#         {"username":"李四","password":"123456789"}
#     ]

# zh = input("请输入账号:")
# mm = input("请输入密码:")

# for i in db:
#     if zh == i.get("username"):
#         if mm == i.get("password"):
#             print("{}登录成功！".format(zh))
#             break
#     else:
#         print("登录失败！")
#     continue    

db = [
        {"username":"张三","password":"123456"},
        {"username":"李四","password":"123456789"}
    ]

zh = input("请输入账号：")
pd = input("请输入密码：")

count = 1
for i in db:
    if zh == i.get("username"):
        i["password"] = pd
        break
    else:
        if len(db) == count:
            db.append({"username":zh,"password":pd})
    count = count + 1    
print(db)    
     

            