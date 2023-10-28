import jsonpath
import pytest

from testcase.test_login import session, yaml, yaml_read



def test_admin_list():
    url='http://a.uzxue.cn/api2/TZsbAdminApi/AdminLoginRecord/GetPage?AdminId=0&PageSize=20&PageIndex=1'
    resp = session.request('get',url=url)
    print(resp.json())
    yaml_read['adminid']=max(jsonpath.jsonpath(resp.json(), '$.data..id'))
    yaml.yaml_write(yaml_read)



def test_admin_del():
    url='http://a.uzxue.cn/api2/TZsbAdminApi/AdminLoginRecord/Deletes'
    head={
        'Content-Type':'application/json; charset=utf-8'
    }
    data=[
   yaml_read['adminid']
    ]
    resp=session.request('post',url=url,json=data,headers=head)
    print(resp.json())