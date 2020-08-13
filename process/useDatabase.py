import MySQLdb
from common.commonMethod import CommonMethod

localCommonMethod = CommonMethod()
baseIp = localCommonMethod.readOpt('database', 'ip')
baseUsername = localCommonMethod.readOpt('database', 'username')
basePassword = localCommonMethod.readOpt('database', 'password')
platformBaseBase = localCommonMethod.readOpt('database', "platform_base")
serviceBaseBase = localCommonMethod.readOpt('database', "service_base")
tenantBaseBase = localCommonMethod.readOpt('database', "tenant_base")


class SelectData:
    def joinPlatformDatabase(self):
        db = MySQLdb.connect(baseIp, baseUsername, basePassword, platformBaseBase)
        return db

    def joinServiceDatabase(self):
        db = MySQLdb.connect(baseIp, baseUsername, basePassword, serviceBaseBase)
        return db

    def joinTenantDatabase(self):
        db = MySQLdb.connect(baseIp, baseUsername, basePassword, tenantBaseBase)
        return db

    def select_user_info(self, what, where, condition):
        db = self.joinPlatformDatabase()
        cursor = db.cursor()
        try:
            sql = "select {} from idaas_user_info where {} = '{}'".format(what, where, condition)
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
        except Exception as e:
            raise e
        finally:
            db.close()

    def select_code_to_account_info(self, account_code):
        db = self.joinTenantDatabase()
        cursor = db.cursor()
        try:
            sql = "select name from idaas_tenant_account where code = '{}'".format(account_code)
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
        except Exception as e:
            raise e
        finally:
            db.close()

    def select_account_info(self, what, where, condition):
        db = self.joinTenantDatabase()
        cursor = db.cursor()
        try:
            sql = "select {} from idaas_tenant_account where {} = '{}'".format(what, where, condition)
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
        except Exception as e:
            raise e
        finally:
            db.close()

    def seleceTenantUserStatus(self, user_id):
        db = self.joinTenantDatabase()
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
        db = self.joinPlatformDatabase()
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

    def select_tenant_info(self, what, where, condition):
        db = self.joinPlatformDatabase()
        cursor = db.cursor()
        sql = "select {} from idaas_tenant_info where {} ='{}'".format(what, where, condition)
        try:
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
        except Exception as e:
            return e
        finally:
            db.close()

    def select_enterprise_info(self, tenant_code):
        db = self.joinPlatformDatabase()
        cursor = db.cursor()
        sql = "SELECT NAME FROM idaas_enterprise_info WHERE id = ( SELECT t.enterprise_id FROM idaas_tenant_enterprise_relation t LEFT JOIN idaas_tenant_info t1 ON t.tenant_Id = t1.id WHERE t1.CODE = '{}')".format(
            tenant_code)
        try:
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
        except Exception as e:
            return e
        finally:
            db.close()
