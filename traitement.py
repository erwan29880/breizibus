from requete import Requete


class Resultat:


    def __init__(self):
        self.__res = Requete()



    def formulaire(self):
        
        return self.__res.requete_ligne()

   

    def traitement(self, req):
        return self.__res.voir_arrets(req), req

