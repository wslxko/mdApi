from common import requestMethod, commonMethod

import json

localRequestMethod = requestMethod.RequestMethod()
localCommonMethod = commonMethod.CommonMethod()


class LoginProcess:
    def login(self, env):
        loginRes = localRequestMethod.login(env)
        token = json.loads(loginRes.text)['result']["token"]
        return token

    def addTokenToHeader(self, env):
        token = self.login(env)
        headers = json.loads(localCommonMethod.readOpt("header", "header"))
        headers["IDAAS-AUTH-TOKEN"] = token
        return headers
