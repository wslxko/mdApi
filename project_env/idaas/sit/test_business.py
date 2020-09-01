import unittest
from common import requestMethod, commonMethod
from process import loginProcess, useDatabase
import ddt
import json
import random

local_request_method = requestMethod.RequestMethod()
local_common_method = commonMethod.CommonMethod()
local_login_process = loginProcess.LoginProcess()
local_use_database = useDatabase.SelectData()
headers = local_login_process.api_header_token()
datas = local_common_method.readExcel("businessApi")


@ddt.ddt
class TestBusiness(unittest.TestCase):

    @ddt.data(*datas[0:2])
    def test_check_unique(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3])
            resultDict = json.loads(result.text)
            self.checkResult(resultDict["message"], datas[4])
        except Exception as e:
            raise e


    @ddt.data(*datas[2:4])
    def test_incremental_user(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3])
            resultDict = json.loads(result.text)
            if resultDict["code"] == "0":
                self.assertNotEquals(resultDict["result"]["total"], datas[4])
            else:
                self.checkResult(resultDict["message"], datas[4])
        except Exception as e:
            raise e

    @ddt.data(*datas[4:6])
    def test_get_user_info(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3])
            resultDict = json.loads(result.text)
            if resultDict["code"] == "11001":
                self.checkResult(resultDict["message"], datas[4])
            elif resultDict["code"] == "0":
                self.checkResult(resultDict["result"]["uid"], datas[4])
        except Exception as e:
            raise e

    @ddt.data(*datas[6:8])
    def test_tenant_login_setting(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3])
            resultDict = json.loads(result.text)
            if resultDict["code"] == "4010":
                self.checkResult(resultDict["message"], datas[4])
            else:
                self.checkResult(len(resultDict["result"]), datas[4])
        except Exception as e:
            raise e


    @ddt.data(*datas[8:10])
    def test_update_tenant(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            json_tenant_data = json.loads(datas[3])
            json_tenant_name = json_tenant_data["tenantName"] + str(random.randint(0, 9))
            json_tenant_data["tenantName"] = json_tenant_name
            result = local_request_method.request(datas[1], uri, headers, json.dumps(json_tenant_data).encode())
            resultDict = json.loads(result.text)
            self.checkResult(resultDict["message"], datas[4])
            if resultDict["code"] == "0":
                base_tenant_name = local_use_database.select_tenant_info("name", "code", json_tenant_data["tenantId"])[
                    0]
                self.checkResult(json_tenant_name, base_tenant_name)
                base_enterprise_name = local_use_database.select_enterprise_info(json_tenant_data["tenantId"])[0]
                self.checkResult(json_tenant_name, base_enterprise_name)
                base_tenant_owner = \
                    local_use_database.select_tenant_info("owner", "code", json_tenant_data["tenantId"])[0]
                base_user_name = local_use_database.select_user_info('name', 'code', base_tenant_owner)[0]
                self.checkResult(json_tenant_name, base_user_name)
            else:
                pass
        except Exception as e:
            raise e


    @ddt.data(*datas[10:12])
    def test_update_account(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            json_user_data = json.loads(datas[3])
            json_user_name = json_user_data["name"] + str(random.randint(0, 9))
            json_user_data["name"] = json_user_name
            result = local_request_method.request(datas[1], uri, headers, json.dumps(json_user_data).encode())
            resultDict = json.loads(result.text)
            self.checkResult(resultDict["message"], datas[4])
            if resultDict["code"] == "0":
                base_account_name = local_use_database.select_code_to_account_info(json_user_data["uid"])[0]
                self.checkResult(json_user_name, base_account_name)
            else:
                pass
        except Exception as e:
            raise e

    def checkResult(self, expect, reality):
        self.assertEqual(expect, reality)


if __name__ == "__main__":
    unittest.main()
