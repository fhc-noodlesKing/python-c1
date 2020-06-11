import pytest, requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import chaxun
from utils.filetools import save

def test_01_login():
    """
        登录成功的测试用例 
    """
    u = "http://122.51.58.214:2333/login"
    d = {"username":"qq296769530","password":"199109xx"}
    res = requests.post(url=u, json=d)

    assert res.status_code == 200
    assert res.json()["status"] == 200

    sql = "select * from t_user where username ='{}'".format(d.get("username"))
    assert len(chaxun(sql)) != 0

    save(res)
 