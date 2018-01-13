import sqlite3

#schema - done
#ext_col
#result fetch - done
#ext queary
#custom queary - done

class db_obj:

    def __init__(self):
        self.__conn = None
        self.__cursor = None
        self.__cur = None
    

    def create_db(self,name):
        try:
            self.__conn = sqlite3.connect(name)
            return "Database is set or created."
        except Exception as e:
            print (e)


    def cur_dsc(self):
        try:
            print (self.__cursor.description)
        except Exception as e:
            print (e)


    def del_data(self,table_name,where_val={},where_key=[]):
        try:
            statement_string1 = "DELETE FROM "+table_name
            i = 0
            if(len(where_val) == len(where_key) == len([])):
                pass
            else:
                if(len(where_val) - len(where_key) != 1):
                         return "Invalid Statement"
                else:
                    statement_string1 += " WHERE "
                    for val in where_val:
                        statement_string1 += str(val)+"="
                        if(type(where_val[val]) != type(0)):
                            statement_string1 += "'{0}'".format(where_val[val])
                        else:
                            statement_string1 += str(where_val[val])
                        if(len(where_key) != len([]) and i<len(where_key)):
                            statement_string1 += " "+str(where_key[i])+" "
                            i+=1
                statement_string1 = statement_string1[:-2:]
            print (statement_string1)
            self.__cursor.execute(statement_string1)
            print ("\nSuccessfullly Executed.\n")
        except Exception as e:
            print (e)
            
    
    def select_data_table(self,table_name,col_names=[],order_by=None,order_by_key=None,limit=None):
        try:
            statement = "SELECT "
            if(len(col_names) == 0):
                statement += "* FROM "+str(table_name)+" "
            else:
                for val in col_names:
                    statement += str(val)+", "
                statement = statement[:-2] +" FROM "+str(table_name)
            if(order_by != None):
                statement += " ORDER BY "
                for val in order_by:
                    statement += str(val) +", "
                if(order_by_key != None):
                    statement = statement[:-2:] + str(order_by_key)
                else:
                #    print (statement)
                    statement = statement[:-2:] + " ASC "
                #    print (statement)
            if(limit != None):
                statement = statement + " LIMIT "+str(limit)
            print (statement)
            qu = self.__cursor.execute(statement)
            from prettytable import PrettyTable
            temp = [description[0] for description in qu.description]
            #print (temp)
            #print (dir(qu))
            t = PrettyTable(temp)
            for val in list(qu.fetchall()):
               t.add_row(val)    
            print (t)
            print ("\nSuccessfullly Executed.\n")
        except Exception as e:
            print (e)
            


    def update_db(self,table_name,set_val,where_val,set_key=[],where_key=[]):
        try:
             statement_string = "UPDATE "+str(table_name)+" SET "
             statement_string1 = " WHERE "
             i = 0
             if(len(set_key) >= len(set_val)):
                 return "Invalid Statement"
             else:
                 for val in set_val:
                     statement_string += str(val)+"="
                     if(type(set_val[val]) != type(0)):
                         statement_string += "'{0}'".format(set_val[val])
                     else:
                         statement_string += str(set_val[val])
                     if(len(set_key) != len([]) and i<len(set_key)):
                         statement_string += " "+str(set_key[i])+" " 
                         i+=1
                     else:
                         statement_string += ", "
             i = 0
             print ("check - 1 ")
             if(len(where_key) >= len(where_val)):
                 return "Invalid Statement"
             else:
                 for val in where_val:
                     statement_string1 += str(val)+"="
                     if(type(where_val[val]) != type(0)):
                         statement_string1 += "'{0}'".format(where_val[val])
                     else:
                         statement_string1 += str(where_val[val])
                     if(len(where_key) != len([]) and i<len(where_key)):
                         statement_string1 += " "+str(where_key[i])+" "
                         i+=1
                     else:
                         statement_string1 += ", "
                 statement_string = statement_string[:-2]+" "+statement_string1[:-2]
             print (statement_string)
             self.__cursor.execute(statement_string)
             print ("Sucessfully Executed.")
        except Exception as e:
                print (e)
               

    def ext_col(*args):
        pass

    def read_schema(self,name=None):
        try:
            temp = []
            if(name == None):
                k = []
                for row in  self.__cursor.execute("select name from sqlite_master where type = 'table'"):
                     k.append(row)
                for l in k:
                    for col in self.__cursor.execute("select sql from sqlite_master where type = 'table' and name = "+"'{0}'".format(l[0])):
                       print (l[0]," : ",col[0])
                       temp.append(str(l[0])+" : "+str(col[0]))
                k.clear()
                del k
                return temp
            else:
                for col in self.__cursor.execute("select sql from sqlite_master where type = 'table' and name = "+"'{0}'".format(name)):
                    print (col[0])
                    temp.append(col[0])
                return temp
        except Exception as e:
            print (e)
            

    def custom_query(self,statement):
        try:
            if("select" in (statement.lower()[:6:])):
                print ((statement.lower()[:6:]))
                qu = self.__cursor.execute(statement)
                from prettytable import PrettyTable
                temp = [description[0] for description in qu.description]
                #print (temp)
                #print (dir(qu))
                t = PrettyTable(temp)
                for val in list(qu.fetchall()):
                   t.add_row(val)    
                print (t)
                print ("\nSuccessfullly Executed.\n")
        
            else:    
                self.__cursor.execute(statement)
                print ("\nSucessfully Excecuted. \n")
        except Exception as e:
            print(e)

    def commit(self):
        try:
            self.__conn.commit()
        except Exception as e:
            print (e)

    @staticmethod
    def get_obj():
        try:
            return db_obj()
        except:
            print ("Problem occurred.")
            return None


    def insert_data(self,table_name,**col_data):
        if(len(col_data) == 0):
            return "Invalid Args."
        else:
            try:
                statement_string = "INSERT INTO "+str(table_name)+" ("
                statement_string1 = " VALUES("
                for col in col_data:
                    statement_string += col +","
                    if(type(col_data[col]) != type(1)):
                        statement_string1 += "'{0}'".format(col_data[col]) +","
                    else:
                        statement_string1 += str(col_data[col]) +","
                statement_string = statement_string[:-1:] + ")"
                statement_string1 = statement_string1[:-1:] + ")"
                print (statement_string+statement_string1)
                self.__cursor.execute(statement_string+statement_string1)
                return "Successfully Inserted."
            except Exception as e:
                print (e)
            

    
    def set_cursor(self):
        try:
            if(self.__cursor is None):
                self.__cursor = self.__conn.cursor()
                return "cursor is set."
            else:
                pass
        except Exception as e:
            print (e)

    def create_table(self,table_name,**col_daty):
        if(len(col_daty) == 0):
            return "Invalid Args."
        else:
            try:
                statement_string = "CREATE TABLE "+str(table_name)+" ("
                for col in col_daty:
                    statement_string += col +" "+col_daty[col]+","
                statement_string = statement_string[:-1:] + ")"
                self.__cursor.execute(statement_string)
                return "Successfully Created."
            except Exception as e:
                print (e)
    
    def close_db(self):
        self.__conn.close()
        self.__cursor = None
        self.__conn = None

    
