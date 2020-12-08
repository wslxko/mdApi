import HTMLReport
import os
import shutil
from datetime import datetime
import unittest
from common import commonMethod
import argparse

localCommonMethod = commonMethod.CommonMethod()

class Parser:
    def parser_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--project", default="idaas", help="project")
        parser.add_argument("-e", "--env", default="dev", help="env")
        args = parser.parse_args()
        return args

    def project(self):
        project = self.parser_args().project
        return project

    def env(self):
        env = self.parser_args().env
        return env


class AllTest(Parser):
    def __init__(self):
        # self.resultPath = os.path.join(localCommonMethod.paths(), 'report', str(datetime.now().strftime("%Y%m%d%H%M%S")))
        self.resultPath = os.path.join(localCommonMethod.paths(), 'report', "autoreport")
        self.caseListFile = os.path.join(localCommonMethod.paths(), "caseFile", "caseFile.txt")
        self.caseFile = os.path.join(localCommonMethod.paths(), "project_env/{}/{}/".format(self.project(), self.env()))
        self.caseList = []

    def set_case_list(self):
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
            fb.close()
        return self.caseList

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:
            case_name = case.split("/")[-1]
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + ".py", top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        shutil.rmtree(os.path.join(localCommonMethod.paths(), 'report'), True)
        suit = self.set_case_suite()
        HTMLReport.TestRunner(
            output_path=self.resultPath,
            report_file_name="测试报告",
            log_file_name="测试运行日志",
            title="测试报告",
            description="测试报告",
            thread_count=3,  # 多线程运行测试用例
            thread_start_wait=3  # 设置线程启动的延迟时间
        ).run(suit)


if __name__ == "__main__":
    obj = AllTest()
    obj.run()
