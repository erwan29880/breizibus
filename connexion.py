import mysql.connector


class Connexion:


    def __init__(self):
        self.__user = 'erwan'
        self.__host = 'localhost'
        self.__port = '3306'
        self.__password = 'root'
        self.__database = 'breizhibus'
        self.cursor = None
        self.conn = None

    
    def ouvrir(self):
        self.conn = mysql.connector.connect(user=self.__user, host=self.__host, password=self.__password, port=self.__port, database=self.__database)
        self.cursor = self.conn.cursor()
    

    def req(self):
        self.ouvrir()
        self.cursor.execute("SHOW TABLES;")
        res = [x for x in self.cursor]
        self.fermer()
        return res


    def commit(self):
        self.ouvrir()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS breizhibus")
        self.conn.commit()
        self.fermer()
               


    def fermer(self):
        self.conn.close()


if __name__ == '__main__':

    co = Connexion()

    co.commit()

    # print(co.req())