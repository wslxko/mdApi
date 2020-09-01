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

    @ddt.data(*datas[4:6])
    def test_check_phone_exist(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3])
            resultDict = json.loads(result.text)
            if resultDict["code"] == "0":
                self.checkResult(datas[4], resultDict["result"])
            else:
                self.checkResult(datas[4], resultDict["message"])
        except Exception as e:
            raise e

    @ddt.data(*datas[6])
    def test_check_third_phone_exist(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3])
            resultDict = json.loads(result.text)
            self.checkResult(datas[4], resultDict["message"])
        except Exception as e:
            raise e

    @ddt.data(*datas[7:9])
    def test_admin_1_create(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3])
            resultDict = json.loads(result.text)
            if resultDict["code"] == "2003":
                self.checkResult(datas[4], resultDict["message"])
            else:
                self.checkResult(datas[4], resultDict["code"])
        except Exception as e:
            raise e

    @ddt.data(*datas[9:11])
    def test_admin_2_delete(self, datas):
        global resultDict, base_user_code
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            if datas[0] == "删除运营中心用户数据-成功":
                base_user_code = local_use_database.select_account_info("code", "name", "autotestluoxk")[0]
                json_data = json.loads(datas[3])
                json_data["uid"] = base_user_code
                result = local_request_method.request(datas[1], uri, headers, json.dumps(json_data))
                resultDict = json.loads(result.text)
                self.checkResult(datas[4], resultDict["message"])
                base_user_deleted = local_use_database.select_account_info("deleted", "code", base_user_code)[0]
                if resultDict["code"] == "0" and base_user_deleted == 1:
                    local_use_database.delete_admin_and_credential("code", base_user_code)
            else:
                result = local_request_method.request(datas[1], uri, headers, datas[3])
                resultDict = json.loads(result.text)
                self.checkResult(datas[4], resultDict["message"])
        except Exception as e:
            raise e

    @ddt.data(*datas[11:13])
    def test_reset_pwd(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3])
            resultDict = json.loads(result.text)
            self.checkResult(datas[4], resultDict["message"])
        except Exception as e:
            raise e

    @ddt.data(*datas[13:16])
    def test_update_attrs(self, datas):
        uri = local_common_method.getUrl("HTTP", "sit", datas[2])
        try:
            result = local_request_method.request(datas[1], uri, headers, datas[3].encode())
            resultDict = json.loads(result.text)
            self.checkResult(resultDict["message"], datas[4])

            if resultDict["code"] == "0":
                base_account_attr = eval(local_use_database.select_account_attr("attributes", "code",
                                                                                json.loads(datas[3])["uid"])[0])["attributesInfo"]
                if len(base_account_attr) != 0:
                    for dict in base_account_attr:
                        if dict["id"] == 1:
                            self.checkResult(json.loads(datas[3])["mobile"], dict["value"])
                        elif dict["id"] == 2:
                            self.checkResult(json.loads(datas[3])["email"], dict["value"])
                else:
                    self.checkResult([], base_account_attr)
        except Exception as e:
            raise e

    def checkResult(self, expect, reality):
        self.assertEqual(expect, reality)


if __name__ == "__main__":
    unittest.main()
