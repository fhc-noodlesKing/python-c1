import requests
from dbtools import chaxun
# url = "http://192.144.148.91:2333/get_title_img?num=3"
# res = requests.get(url)
# print(res.text)

# u = "http://superf.xyz:2333/login"

# d = {"username":"qq296769530","password":"199109xx"}
# res = requests.post(url=u, json=d)

# assert res.status_code == 200
# assert res.json()["status"] == 200

# sql = "select * from t_user where username = '{}'".format(d.get("username"))
# if len(chaxun(sql)) !=0:
#     print("结果测试通过！")
# else:
#     print("接口测试失败！")    

u = "http://superf.xyz:2333/get_title_img?num=3"
res = requests.request("get",url=u)

u1 = "http://superf.xyz:2333/login"
d1 = {"username":"qq296769530","password":"199109xx"}
res = requests.request("post", url=u1, json=d1)
print(res.text)










# print(res.text)

# token = res.json()["data"]["token"]

# u1 = "http://superf.xyz:2333/comment/new"
# d1 = {"ctype":3, "comment":"奥克斯空调好用", "fid":"63022"}
# h1 = {"token":token}
# res = requests.post(url=u1, json=d1, headers=h1)
# print(res.text)