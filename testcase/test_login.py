import json
import logging
import allure
import pytest
import requests
from Yaml_ulit import Yaml_Ulit

session = requests.Session()
yaml = Yaml_Ulit('shuju.yaml')
yaml_read = yaml.yaml_read() or {}


# 登录接口
@pytest.mark.run(order=1)
@pytest.mark.parametrize("data", [Yaml_Ulit(r"D:\pythonProject4\testcase\login.yaml").yaml_read()])
def test_login(data):
    url = 'http://a.uzxue.cn/api1/connect/token'
    data = {
        'grant_type': data['grant_type'],
        'client_id': data['client_id'],
        'client_secret': data['client_secret'],
        'loginName': data['loginName'],
        'loginPwd': data['loginPwd'],
    }
    resp = session.request('post', url=url, data=data)
    # if 'access_token' in resp.json():
    yaml_read['access_token'] = resp.json()['access_token']
    yaml.yaml_write(yaml_read)
    print(resp.json())
    session.headers = {
        'Authorization': f'Bearer {yaml.yaml_read()["access_token"]}'
    }
    assert 'access_token' in resp.json() and resp.status_code == 200
# session.headers = {
#         'Authorization': f'Bearer {yaml.yaml_read()["access_token"]}'
#     }

# session.headers = {
#         'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkM0MUY1REE5ODQxN0NEMTkxRENCNDdCMDg2Q0JDMzAwM0QzMkNDRkVSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6InhCOWRxWVFYelJrZHkwZXdoc3ZEQUQweXpQNCJ9.eyJuYmYiOjE2OTc0OTUwMDAsImV4cCI6MTY5NzUwMTAwMCwiaXNzIjoiaHR0cDovL3Rva2VuLnV6eHVlLmNuIiwiYXVkIjoiaHVpaGFuZ2VkdSIsImNsaWVudF9pZCI6Imh1aWhhbmctYWRtaW4iLCJzdWIiOiIxNTA3MTI2NzU5MCIsImF1dGhfdGltZSI6MTY5NzQ2NTcyNywiaWRwIjoibG9jYWwiLCJpZCI6IjE2MjQiLCJuYW1lIjoiJWU1JTg4JTk4JWU1JTg2JWFjIiwicGhvbmVfbnVtYmVyIjoiMTUwNzEyNjc1OTAiLCJyb2xlIjoiMTAxMyIsImp0aSI6IjhEMDc2MEI3MzU3OTZBMjI3QTVCREQwNERCNzNFNDY5IiwiaWF0IjoxNjk3NDY1NzI3LCJzY29wZSI6WyJodWloYW5nc2NvcGUiLCJvcGVuaWQiLCJwcm9maWxlIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbImFkbWlucGFzc3dvcmQiXX0.De1obomAER45OoV8mM2EJgLw2vIjh89MNbzp7dPZRO4n3kd3Hu924Cq9pG8T1w7eMOILD31-neQA4V3xu1r_C1iiRPLzjONk9aon-y2jKVEAYRoRhK33zQuEQzZ5rWmj2N9cH_FUr2j50S7Y92edeymZgk_9CS6FDSAHzjnYYRnT2TQTErg3eKxa8hljOs3RXwd-vcYDoMraIBDOYk8E_RLjSUYPif5_5om7QUJiVrI_QFWXEZQUP0CEK6OK4l6Ikvo4cq6y5nXvRYxtq2Ey4NmDmJp9Sr_AJ-iBiuB8c7iVLvUSy9YbKB7OroLCGgLa7wZ7SebQK9yIvvVDJvLnNA'
#      }








