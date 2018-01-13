import pysftp as sftp
import paramiko



#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.load_system_host_keys()
#ssh.connect("192.168.80.137", username='yash1', password='yash1')


#example -
'''

source - file: hello.txt
destination - file: /hello/hello.txt

'''

#change in __init__ file of pysftp and comment the key verify section


class sftp_obj:

    def __init__(self):
        self.__host = None
        self.__username = None
        self.__password = None
        self.__connection = None
        self.__cnopts = None
        



    def set_connection(self,host,username,password):
        try:
            self.__host = host
            self.__username = username
            self.__password = password
            #client = paramiko.SSHClient()
            self.__cnopts = sftp.CnOpts()
            #print ("hello")
            self.__cnopts.hostkeys = None
            self.__connection = sftp.Connection(
                self.__host,
                username = self.__username,
                password = self.__password,
                cnopts=self.__cnopts)
            print ("Connection successfully set.\n")
        except Exception as e:
            print (e)


    def change_connection(self,host=None,username=None,password=None):
        try:
            flag = False
            if(host is not None):
                self.__host = host
                flag = True
            if(username is not None):
                self.__username = username
                flag = True
            if(password is not None):
                self.__password = password
                flag = True
            if(flag):
                self.__connection.close()
                self.__connection = sftp.Connection(
                    self.__host,
                    self.__username,
                    self.__password )
                print ("Connection successfully changed\n")
            else:
                print ("No change required.\n")
        except Exception as e:
            print (e)

    def push_file(self,source_path,destination_path):
        try:
            self.__connection.put(source_path,destination_path)
            print ("Success\n")
        except Exception as e:
            print (e)


    def pull_file(self,source_path,destination_path):
        try:
            self.__connection.get(source_path,destination_path)
            print ("Success\n")
        except Exception as e:
            print (e)

    def close_connection(self):
        try:
            self.__host = None
            self.__username = None
            self.__password = None
            self.__cnopts = None
            self.__connection.close()
            self.__connection = None
        except Exception as e:
            print (e)
