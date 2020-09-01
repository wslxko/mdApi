import unittest, ddt, json
from common import commonMethod, requestMethod
from process import loginProcess, useDatabase

local_request_method = requestMethod.RequestMethod()
local_common_method = commonMethod.CommonMethod()
local_login_process = loginProcess.LoginProcess()
local_use_database = useDatabase.SelectData()
headers = local_login_process.api_header_token()
datas = local_common_method.readExcel("syncApis")


@ddt.ddt
class TestOpertionRoles(unittest.TestCase):
    @ddt.data(*datas[0:2])
    def test_user_ak_sync(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3])
            result_dict = json.loads(result.text)
            if "records" in result_dict["result"].keys():
                self.checkResult(len(result_dict["result"]["records"]), datas[4])
            else:
                self.checkResult(result_dict["result"]["total"], datas[4])
        except Exception as e:
            raise e

    @ddt.data(*datas[2:4])
    def test_user_info_sync(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3])
            result_dict = json.loads(result.text)
            if "records" in result_dict["result"].keys():
                self.checkResult(len(result_dict["result"]["records"]), datas[4])
            else:
                self.checkResult(result_dict["result"]["total"], datas[4])
        except Exception as e:
            raise e

    @ddt.data(*datas[4:6])
    def test_user_roles_sync(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3])
            result_dict = json.loads(result.text)
            if "records" in result_dict["result"].keys():
                self.checkResult(len(result_dict["result"]["records"]), datas[4])
            else:
                self.checkResult(result_dict["result"]["total"], datas[4])
        except Exception as e:
            raise e

    @ddt.data(datas[6])
    def test_opertion_admin_sync(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3].encode())
            result_dict = json.loads(result.text)
            data_result = local_use_database.select_keyword_admin_number()[0]
            self.checkResult(result_dict["result"]["total"], data_result)
        except Exception as e:
            raise e

    @ddt.data(datas[7])
    def test_tenant_sync(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3].encode())
            result_dict = json.loads(result.text)
            data_result = local_use_database.select_oss_tenant_number()[0]
            self.checkResult(len(result_dict["result"]), data_result)
        except Exception as e:
            raise e

    @ddt.data(*datas[8:10])
    def test_user_sync(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3].encode())
            result_dict = json.loads(result.text)
            if result_dict["code"] == "4004":
                self.checkResult(datas[4], result_dict["message"])
            else:
                data_result = local_use_database.select_service_tenant_user_number()[0]
                self.checkResult(result_dict["result"]["total"], data_result)
        except Exception as e:
            raise e

    def checkResult(self, expect, reality):
        self.assertEqual(expect, reality)


if __name__ == "__main__":
    unittest.main()
