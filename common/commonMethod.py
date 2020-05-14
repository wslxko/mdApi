import configparser
import os
import xlrd


class CommonMethod:
    def paths(self):
        paths = os.path.split(os.path.dirname(__file__))[0]
        return paths

    def readOpt(self, section, option):
        path = os.path.join(self.paths(), "config.ini")
        cf = configparser.ConfigParser()
        cf.read(path)
        value = cf.get(section, option)
        return value

    def readExcel(self, sheetName):
        cls = []
        data = xlrd.open_workbook(os.path.join(self.paths(), "casefile/testdata.xlsx"))
        sheet = data.sheet_by_name(sheetName)
        rowNum = sheet.nrows
        for index in range(1, rowNum):
            cls.append(sheet.row_values(index))
        return cls

    def getUrl(self, section, option, url):
        host = self.readOpt(section, option)
        uri = host + url
        return uri
