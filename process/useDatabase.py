import MySQLdb
from common.commonMethod import CommonMethod

localCommonMethod = CommonMethod()
baseIp = localCommonMethod.readOpt('database', 'ip')
baseUsername = localCommonMethod.readOpt('database', 'username')
basePassword = localCommonMethod.readOpt('database', 'password')
baseBase = localCommonMethod.readOpt('database', 'base')


class SelectData:
    def joinDatabase(self):
        db = MySQLdb.connect(baseIp, baseUsername, basePassword, baseBase)
        return db

    def selectUserInfo(self, username):
        db = self.joinDatabase()
        cursor = db.cursor()
        try:
            sql = "select id from idaas_user_info where user_name = '{}'".format(username)
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
        except Exception as e:
            raise e
        finally:
            db.close()

    def seleceTenantUserStatus(self, user_id):
        db = self.joinDatabase()
        cursor = db.cursor()
        try:
            sql = "select status from idaas_tenant_user where user_id = '{}'".format(user_id)
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
        except Exception as e:
            raise e
        finally:
            db.close()

    def deleteUser(self, user_name):
        db = self.joinDatabase()
        cursor = db.cursor()
        try:
            sql = "delete u,t from idaas_user_info u left join idaas_tenant_user t on u.id = t.user_id where u.user_name = '{}'".format(
                user_name)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()