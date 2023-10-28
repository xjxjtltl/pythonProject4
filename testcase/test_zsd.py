import jsonpath as jsonpath
import pytest
import allure
from Yaml_ulit import Yaml_Ulit
from testcase.test_login import session

yaml = Yaml_Ulit('shuju.yaml')
yaml_read = yaml.yaml_read() or {}


class Testzsd:

    #新增知识点
    @allure.step("发送接口请求并获取响应数据")
    def test_add_Knowledge_points(self):
        url = 'http://a.uzxue.cn/api2/TZsbAdminProductApi/KnowledgePoint/Insert'
        data = {
            "id": 0,
            "name": "测试1",
            "superiorId": 0,
            "tdkTitle": "页面TDK标题",
            "tdkKeywords": ["页面TDK关键字"],
            "tdkDescription": "页面TDK描述"
        }
        resp = session.request('post', url=url, json=data)
        print(resp.json())
        allure.attach(str(resp.json()), name="Response Data", attachment_type=allure.attachment_type.JSON)
        allure.attach(str(resp.headers), name="Response Data", attachment_type=allure.attachment_type.JSON)
        allure.attach(str(resp.status_code), name="Response Data", attachment_type=allure.attachment_type.JSON)
        allure.attach(str(data), name="Response Data", attachment_type=allure.attachment_type.JSON)
        assert '操作成功' in resp.text and resp.status_code == 200

    # 知识点列表
    @allure.step("发送接口请求并获取响应数据")
    def test_list_Knowledge_points(self):
        url = 'http://a.uzxue.cn/api2/TZsbAdminProductApi/KnowledgePoint/GetKnowledgePointTree'
        resp = session.request('get', url=url)
        print(resp.json())
        # if '获取成功' in resp.json():
        yaml_read['zsd_id'] = max(jsonpath.jsonpath(resp.json(), '$.result..id'))
        yaml.yaml_write(yaml_read)
        print(yaml_read['zsd_id'])
        allure.attach(str(resp.json()), name="Response Data", attachment_type=allure.attachment_type.JSON)
        assert '获取成功' in resp.text and resp.status_code == 200

    @allure.step("发送接口请求并获取响应数据")
    def test_list_Knowledge_points2(self):
        url = 'http://a.uzxue.cn/api2/TZsbAdminProductApi/KnowledgePoint/GetKnowledgePointTree'
        resp = session.request('get', url=url)
        print(resp.json())
        # if '获取成功' in resp.json():
        yaml_read['zsd_id2'] = min(jsonpath.jsonpath(resp.json(), '$.result..id'))
        yaml.yaml_write(yaml_read)
        print(yaml_read['zsd_id2'])
        allure.attach(str(resp.json()), name="Response Data", attachment_type=allure.attachment_type.JSON)
        assert '获取成功' in resp.text and resp.status_code == 200

# 编辑知识点
    @allure.step("发送接口请求并获取响应数据")
    def test_edit_Knowledge_points(self):
        url = 'http://a.uzxue.cn/api2/TZsbAdminProductApi/KnowledgePoint/EditName'
        data = {
            "id": yaml_read["zsd_id"],
            "name": "测试",
            "superiorId": 0,
            "orders": 3,
            "tdkTitle": "页面TDK标题",
            "tdkKeywords": ["页面TDK关键字"],
            "tdkDescription": "页面TDK描述"
        }
        resp = session.request('post', url=url, json=data)
        print(resp.json())
        allure.attach(str(resp.json()), name="Response Data", attachment_type=allure.attachment_type.JSON)
        assert '操作成功' in resp.text and resp.status_code == 200


    # 删除知识点
    @allure.step("发送接口请求并获取响应数据")
    @pytest.mark.usefixtures()
    def test_del_Knowledge_points(self):
        url = f'http://a.uzxue.cn/api2/TZsbAdminProductApi/KnowledgePoint/Delete?id={yaml_read["zsd_id"]}'
        resp = session.request('post', url=url)
        print(resp.json())
        allure.attach(str(resp.json()), name="Response Data", attachment_type=allure.attachment_type.JSON)
        assert '操作成功' in resp.text and resp.status_code == 200
