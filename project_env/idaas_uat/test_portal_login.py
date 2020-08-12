from common import commonMethod, requestMethod
import unittest
import ddt

local_common_method = commonMethod.CommonMethod()
local_request_method = requestMethod.RequestMethod()
test_datas = []


@ddt.ddt
class request_login(unittest.TestCase):
    @ddt.data(*test_datas)
    def test_1_portal(self, test_datas):
        uri = "http://clouduat.meicloud.com/portal/fil/check-phone"
