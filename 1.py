import MySQLdb
import xlrd
import os

# path = os.path.join('/Users/geiniyituoxiang/midea/idaas/自动化脚本/api/', "1.xlsx")
# xls = xlrd.open_workbook(path)
# sheet = xls.sheet_by_name('Sheet1')
#
# caseList = []
# rowNums = sheet.nrows
# for index in range(1, rowNums):
#     caseList.append(sheet.row_values(index))
#
# mcList = []
# for i in caseList:
#     mcList.append(i[19])
#
# baseIp = '3306-W-T-IAM-PRD-01-MYC1.service.dcnh.consul'
# baseUsername = 'idaas'
# basePassword = 'vexh83vXU'
# baseBase = 'idaas_v3_tenant'
# db = MySQLdb.connect(baseIp, baseUsername, basePassword, baseBase)
# cursor = db.cursor()
#
# sql = '''SELECT code FROM idaas_tenant_account WHERE sources='A002' AND STATUS='1' AND deleted="0"'''
#
# result = cursor.execute(sql)
#
# db_list = []
# db_result = cursor.fetchall()
# for mc in db_result:
#     db_list.append(mc[0])
#
#
# result_list = []
# for exist_mc in mcList:
#     if exist_mc not in db_list:
#         result_list.append(exist_mc)
# print(result_list)

a = {'code': '11001', 'message': '账号不存在'}
print(type(a))
print('code' not in a.keys())