import MySQLdb


class SelectData:
    def selectUserInfo(self, username):
        db = MySQLdb.connect("10.16.81.213", "root", "Idaas@2020", "idaas_sit")
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
        db = MySQLdb.connect("10.16.81.213", "root", "Idaas@2020", "idaas_sit")
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
        db = MySQLdb.connect("10.16.81.213", "root", "Idaas@2020", "idaas_sit")
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
