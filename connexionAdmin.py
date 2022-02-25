import mysql.connector


class Connexion:


    def __init__(self):
        self.__user = 'erwan'
        self.__host = 'localhost'
        self.__port = '3306'
        self.__password = 'root'
        self.__database = 'users'
        self.cursor = None
        self.conn = None

    
    def ouvrir(self):
        self.conn = mysql.connector.connect(user=self.__user, host=self.__host, password=self.__password, port=self.__port, database=self.__database)
        self.cursor = self.conn.cursor()
    

    def fermer(self):
        self.conn.close()


if __name__ == '__main__':

    co = Connexion()

    co.commit()

    # print(co.req())