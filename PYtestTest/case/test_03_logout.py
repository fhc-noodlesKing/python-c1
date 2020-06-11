import pytest
import requests
from utils.filetools import read

def test_01_logout():
    token = read()
    u = "http://122.51.58.214:2333/logout"
    h = {"Content-Type":"application/json","token":token}
    res = requests.get(url=u,headers=h)
    print(res.text)