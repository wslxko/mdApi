from common import requestMethod, commonMethod

import json

localRequestMethod = requestMethod.RequestMethod()
localCommonMethod = commonMethod.CommonMethod()


class LoginProcess:
    def getToken(self, env):
        loginRes = localRequestMethod.login(env)
        token = json.loads(loginRes.text)['result']["token"]
        return token

    def addTokenToHeader(self, env):
        token = self.getToken(env)
        headers = json.loads(localCommonMethod.readOpt("header", "header"))
        headers["IDAAS-AUTH-TOKEN"] = token
        return headers

    def api_header_token(self):
        return {"Content-Type": "application/json",
                "X-IDaaS-APPID": "lXmWrDHxFfGI7OQ7d81iMvIr",
                "X-IDaaS-TOKEN": "9mq5izwm.8c180fb5c69263632db0d6a6e3dff0eb148ea7e191854b05a662436fb407209630497760d017c8a5039e40f9d5a0e13ea6aa940ba423113796555e8b7f36db6d.1597287784698"}
