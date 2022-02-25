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




    def voir_arrets(self, ligne):
        """ligne est la réponse issue du formulaire, soit le nom de la ligne de bus, par exemple Bleu, Vert etc"""

        self.ouvrir()
       
        sql = f"SELECT arrets.nom FROM arrets JOIN arrets_lignes ON arrets.id_arret=arrets_lignes.id_arret JOIN lignes ON arrets_lignes.id_ligne=lignes.id_ligne WHERE lignes.nom='{ligne}'"
        self.cursor.execute(sql)
        res = [x for x in self.cursor]

        self.fermer()
        return res


    


    def voir_bus(self, ligne):

        "voir les bus par ligne"

        self.ouvrir()
       
        sql = f"SELECT numero FROM bus JOIN lignes ON lignes.id_ligne=bus.id_ligne WHERE lignes.nom='{ligne}';"
        self.cursor.execute(sql)
        res = [x for x in self.cursor]

        self.fermer()
        return res



    def voir_bus2(self):
    
        "voir les bus"

        self.ouvrir()
       
        self.cursor.execute("SELECT id_bus, numero FROM bus;")
        res = [x for x in self.cursor]

        self.fermer()
        return res



    def supprimer_bus(self, bus):

        self.ouvrir()

        bus = int(bus)

        sql = f"DELETE FROM bus WHERE id_bus={bus};"
        
        self.cursor.execute(sql)
        self.conn.commit()
        self.fermer()
        




if __name__ == "__main__":

    a=Administration()

    a.commit('gtref', 11, 'Bleu')
    # a.supprimer_bus('12')