import MySQLdb as mdb

#if you want to connect database in remote place
#change cnf file of mysql/mariaDB
#from bind address 127.0.0.1 / localhost to
#0.0.0.0 or comment that statement


class mysql_obj:

    def __init__(self):
        self.__conn = None
        self.__cursor = None


    def connection(self,host,user,password,database):
        try:
            if(host is not None and
               user is not None and
               password is not None and
               database is not None):
                self.__conn = mdb.connect(host=host,
                                          user=user,
                                          password = password,
                                          db = database)

            else:
                print ("None not valid.")
        except Exception as e:
            print (e)


    def set_cursor(self):
        try:
            if (self.__conn is not None):
                self.__cursor = self.__conn.cursor()
            else:
                print ("Invalid entry")
        except Exception as e:
            print (e)

    @staticmethod
    def get_obj():
        return mysql_obj()


    def close_connection(self):
        self.__conn.close()
        self.__cursor = None
        self.__conn = None


    def commit(self):
        self.__conn.commit()

    
    def execute(self,statement):
        try:
            if(self.__cursor is not None):
                self.__cursor.execute(statement)
            else:
                print ("Cursor is not set")
        except Exception as e:
            print (e)
