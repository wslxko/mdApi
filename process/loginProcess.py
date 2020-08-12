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
                "X-IDaaS-APPID": "g8Fuu6CAire4JeAqabLbS3cw",
                "X-IDaaS-TOKEN": "nj8dmzqzvm.97d7591622219cc74a238bff970f54a0051651d8fcfb263a0b02bae14bdbaaae07c584f21c346fa9dfc7c19ee00fdaa42dc684f7de40140d0c3d4c54ff169ef9.1597053296574"}
