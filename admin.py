import mysql.connector
from connexion import Connexion


class Administration(Connexion):

    """ Affichage des lignes de bus sur la page d'accueil (requete_ligne) afin de visualiser tous les arrets (voir_arret)"""

    def __init__(self):
       super().__init__()
    

    
    def commit(self, immat, places, ligne):
        
        self.ouvrir()


        numeros = self.cursor.execute("SELECT id_bus FROM bus ORDER BY id_bus DESC LIMIT 1;")
        numeros =str([x for x in self.cursor][0][0])
        numeros = 'BB'+numeros

        sql = f"SELECT lignes.id_ligne FROM lignes JOIN bus ON lignes.id_ligne=bus.id_ligne WHERE lignes.nom = '{ligne}';"
        id_ligne = self.cursor.execute(sql)
        id_ligne = [x for x in self.cursor][0][0]

        sql = "INSERT INTO bus(numero, immatriculation, nombre_place, id_ligne)values(%s,%s,%s,%s);"
        val = (numeros, immat, places, id_ligne)

        self.cursor.execute(sql, val)
        self.conn.commit()


        self.fermer()
        

if __name__ == "__main__":

    a=Administration()

    a.commit('gtref', 11, 'Bleu')