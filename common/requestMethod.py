import requests
import json
from common import commonMethod

localCommonMethod = commonMethod.CommonMethod()


class RequestMethod:
    def post(self, url, headers, data):
        res = requests.post(url=url, headers=headers, data=data)
        return res

    def get(self, url, headers, data):
        res = requests.get(url=url, headers=headers, params=data)
        return res

    def delete(self, url, headers, data):
        res = requests.delete(url=url, headers=headers, data=data)
        return res

    def request(self, method, url, headers, data):
        if method == "post":
            res = self.post(url, headers, data)
        elif method == "get":
            res = self.get(url, headers, data)
        else:
            res = self.delete(url, headers, data)
        return res

    def login(self, env):
        headers = {"Content-Type": "application/json"}
        data = {
            "username": "MC000000019",
            "password": "HDcJZSZbsNRdn5DikBEltw==",
            "sid": "20"
        }
        url = localCommonMethod.getUrl("HTTP", env, "/user/login")
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        return res
