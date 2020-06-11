import pytest, requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import chaxun

def test_01_lbt():
    url = "http://122.51.58.214:2333/get_title_img?num=3"
    res = requests.get(url)

    assert res.status_code == 200 and res.json()["status"] == 200

    id = res.json()["data"][0]["id"]
    sql = "select * from t_title_img where id ={}".format(id)
    assert len(chaxun(sql)) != 0