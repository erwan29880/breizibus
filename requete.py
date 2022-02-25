import mysql.connector
from connexion import Connexion


class Requete(Connexion):

    """ Affichage des lignes de bus sur la page d'accueil (requete_ligne) afin de visualiser tous les arrets (voir_arret)"""

    def __init__(self):
       super().__init__()


    def requete_ligne(self):
        

        self.ouvrir()
        
        self.cursor.execute("SELECT nom FROM lignes ORDER BY id_ligne DESC")
        res = [x for x in self.cursor]

        self.fermer()
        return res



    def voir_arrets(self, ligne):
        """ligne est la réponse issue du formulaire, soit le nom de la ligne de bus, par exemple Bleu, Vert etc"""

        self.ouvrir()
       
        sql = f"SELECT arrets.nom, arrets.adresse FROM arrets JOIN arrets_lignes ON arrets.id_arret=arrets_lignes.id_arret JOIN lignes ON arrets_lignes.id_ligne=lignes.id_ligne WHERE lignes.nom='{ligne}'"
        self.cursor.execute(sql)
        res = [x for x in self.cursor]

        self.fermer()
        return res, ligne


