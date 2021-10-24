import mysql.connector

class Database:
    def __init__(self,host,user,pwd,database):
        self.__host = host
        self.__user = user
        self.__password = pwd
        self.__database = database
        self.__connection = None
        self.__cursor = None
    
    def createConnection(self):
        self.__connection = mysql.connector.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            database = self.__database
        )
        self.__cursor = self.__connection.cursor()
    
    def getConnection(self):
        return {"connection":self.__connection,"cursor":self.__cursor}
    
    def closeConnection(self):
        self.__connection.close()
        self.__cursor.close()

