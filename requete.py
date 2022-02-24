import mysql.connector
from connexion import Connexion


class Requete(Connexion):


    def __init__(self):
       super().__init__()

    def req(self):
        self.ouvrir()

        self.cursor.execute("select nom from personnes2 where id_personne=7")

        res = [x for x in self.cursor]

        self.fermer()
        return res

    
if __name__ == '__main__':

    co = Requete()




    print(co.req())