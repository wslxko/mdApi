import unittest, ddt, json
from common import commonMethod, requestMethod
from process import loginProcess, useDatabase

local_common_method = commonMethod.CommonMethod()
local_request_method = requestMethod.RequestMethod()
local_login_process = loginProcess.LoginProcess()
local_use_database = useDatabase.SelectData()
datas = local_common_method.readExcel("opertionAdmin")
headers = local_login_process.api_header_token()


@ddt.ddt
class TestOpertionAdmin(unittest.TestCase):
    @unittest.skip
    @ddt.data(*datas[0:2])
    def test_disable_admin(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3])
            resultDict = json.loads(result.text)
            self.checkResult(resultDict["message"], datas[4])

            json_user_data = json.loads(datas[3])
            json_user_id = json_user_data["uid"]
            if resultDict["code"] == "0":
                base_user_status = local_use_database.select_account_info("status", "code", json_user_id)[0]
                self.checkResult(base_user_status, 2)
            else:
                pass
        except Exception as e:
            raise e

    @ddt.data(*datas[2:4])
    def test_enable_admin(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3])
            resultDict = json.loads(result.text)
            self.checkResult(resultDict["message"], datas[4])
            if resultDict["code"] == "0":
                json_user_data = json.loads(datas[3])
                json_user_id = json_user_data["uid"]
                base_user_status = local_use_database.select_account_info("status", "code", json_user_id)[0]
                self.checkResult(base_user_status, 1)
            else:
                pass
        except Exception as e:
            raise e

    def checkResult(self, expect, reality):
        self.assertEqual(expect, reality)


if __name__ == "__main__":
    unittest.main()
