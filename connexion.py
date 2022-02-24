import mysql.connector


class Connexion:


    def __init__(self):
        self.user = 'erwan'
        self.host = 'localhost'
        self.port = '3306'
        self.password = 'root'
        self.database = 'breizhibus'
        self.cursor = None
        self.conn = None

    
    def ouvrir(self):
        self.conn = mysql.connector.connect(user=self.user, host=self.host, password=self.password, port=self.port, database=self.database)
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