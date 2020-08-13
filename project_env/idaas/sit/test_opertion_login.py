from common import commonMethod, requestMethod
import unittest

local_common_method = commonMethod.CommonMethod()
local_request_method = requestMethod.RequestMethod()

user_name = "luoxk3"
password = "123456"

class opertion_login(unittest.TestCase):
    def test_check_phone(self):
        uri = local_common_method.getUrl("HTTP", "sit", "/admin/api/user/check")
        headers = {}
        params = {"account": "luoxk3"}
        result = local_request_method.get(uri, headers, params)
        print(result)


if __name__ == "__main__":
    unittest.main()
