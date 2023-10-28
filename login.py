import requests
from Yaml_ulit import Yaml_Ulit

session = requests.Session()
file = Yaml_Ulit('shuju.yaml')
file_data=file.yaml_read() or {}

# session.headers = {
#     'Authorization': f'Bearer {Yaml_file.yaml_read()["access_token"]}'
# }
try:
    session.headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {file.yaml_read()["access_token"]}'
    }
except:
    def test_login():
        url = 'https://api.tttt.one/rest-v2/login/access_token'
        data = {
            "password": "12345678",
            "email": "dadada@163.com"
        }
        resp = session.request('post', url=url, json=data)
        # access_token = resp.json()['access_token']
        file_data['access_token'] = resp.json()['access_token']
        file.yaml_write(file_data)
        # access_token = {
        #     'access_token': access_token
        # }
        # file.yaml_write(access_token)
        print(resp.json())

# 注册接口
# def test_register():
#     url = 'https://api.tttt.one/rest-v2/login/sign_up'
#     data = {
#         "password": "12345678",
#         "email": "dadada@163.com"
#     }
#
#     resp = session.request('post', url=url,json=data)
#     print(resp.json())
#     assert 'id' in resp.json() and resp.status_code == 200

# 登录接口
def test_login():
    url = 'https://api.tttt.one/rest-v2/login/access_token'
    data = {
        "password": "12345678",
        "email": "dadada@163.com"
    }
    resp = session.request('post', url=url, json=data)
    # access_token = resp.json()['access_token']
    file_data['access_token']=resp.json()['access_token']
    file.yaml_write(file_data)
    # access_token = {
    #     'access_token': access_token
    # }
    # file.yaml_write(access_token)
    print(resp.json())


# 创建任务接口接口
def test_add_tast():
    url = 'https://api.tttt.one/rest-v2/todo'
    data = {
        "title": "第一个任务",
        "is_done": False
    }
    resp = session.request('post', url=url, json=data)
    print(resp.json())
    assert 'title' in resp.json() and resp.status_code == 200


# 查询任务列表接口
def test_tast_list():
    url = 'https://api.tttt.one/rest-v2/todo'
    resp = session.request('get', url=url)
    print(resp.json())
    ids = max([item['id'] for item in resp.json()['items']])
    file_data['id'] = ids
    file.yaml_write(file_data)
    # id = {'id': ids}
    # file.yaml_write(id)
    # print(ids)
    # for ids in resp.json()['items']:
    #         id=ids['id']
    #         print(id)
    # print(resp.json()['items'][0]['id'])
    # id=resp.json()['items']['id']
    # print(id)
    # id={'id':id}
    # file.yaml_write(id)

    assert 'items' in resp.json() and resp.status_code == 200


# 任务详情接口
def test_details_tast():
    url = f'https://api.tttt.one/rest-v2/todo/{file_data["id"]}'
    resp = session.request('get', url=url)
    print(resp.json())
    assert resp.status_code == 200


# 修改任务接口
def test_xiugai_tast():
    url = f'https://api.tttt.one/rest-v2/todo/{file_data["id"]}'
    data = {
        "title": "修改第一个任务",
        "is_done": False
    }
    resp = session.request('put', url=url, json=data)
    print(resp.json())
    assert resp.status_code == 200


# 删除任务接口  # def test_del_tast():
def test_tast_list2():
    url = f'https://api.tttt.one/rest-v2/todo/{file_data["id"]}'
    resp = session.request('DELETE', url=url)
    print(resp.text)
