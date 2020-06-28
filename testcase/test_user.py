import unittest
import ddt
from common import commonMethod, requestMethod
from process import loginProcess, globalData, useDatabase
import json
import time

localCommonMethod = commonMethod.CommonMethod()
localRequestMethod = requestMethod.RequestMethod()
localLoginProcess = loginProcess.LoginProcess()
localUserDatabase = useDatabase.SelectData()
testDatas = localCommonMethod.readExcel("user")


@ddt.ddt
class TestLogin(unittest.TestCase):
    @ddt.data(*testDatas[0:2])
    def test_1_CreateSubAccount(self, testDatas):
        global resultDict
        headers = localLoginProcess.addTokenToHeader(globalData.env)
        uri = localCommonMethod.getUrl("HTTP", globalData.env, testDatas[2])
        try:
            result = localRequestMethod.request(testDatas[1], url=uri, headers=headers, data=testDatas[3])
            resultDict = json.loads(result.text)
        except Exception as e:
            return e
        finally:
            self.checkResult(resultDict["code"], testDatas[4])

    @ddt.data(*testDatas[2:4])
    def test_2_deleteSubAccount(self, testDatas):
        global resultDict, dbResult
        data = {"userId": str(localUserDatabase.selectUserInfo(testDatas[3])[0])}
        headers = localLoginProcess.addTokenToHeader(globalData.env)
        uri = localCommonMethod.getUrl("HTTP", globalData.env, testDatas[2])
        try:
            result = localRequestMethod.request(testDatas[1], uri, headers, json.dumps(data))
            resultDict = json.loads(result.text)
            user_id = localUserDatabase.selectUserInfo(testDatas[3])
            dbResult = localUserDatabase.seleceTenantUserStatus(user_id[0])
        except Exception as e:
            raise e
        finally:
            localUserDatabase.deleteUser(testDatas[3])
            self.checkResult(resultDict["code"], '0')
            self.checkResult(dbResult[0], 0)

    def checkResult(self, expect, reality):
        self.assertEqual(expect, reality)


if __name__ == "__main__":
    unittest.main()
