from dbtools import chaxun, commit


# username = input("请输入账号：")
# password = input("请输入密码：")

# sql = 'select * from t_admin where username="{}" and password ="{}"'.format(username,password)
# print(sql)
# res = chaxun(sql)

# if len(res) != 0:
#     print("管理员登陆成功！")
# else:
#     print("管理员登陆失败！")    

#-------------------------------------------注册-----------------------------------------
username = input("请输入账号：")
password = input("请输入密码：")

sql = 'INSERT into t_admin values(NULL, "{}", "{}", NULL, NULL, NULL, NULL, NULL, NULL,0, NULL, NULL, NULL)'.format(username,password)
res = commit(sql)
if res == True:
    sql = 'select * from t_admin where username="{}" and password="{}"'.format(username,password)
    res = chaxun(sql)
    if len(res) != 0:
        print("注册成功")
else:
    print("注册失败")    