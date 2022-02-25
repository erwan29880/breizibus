import bcrypt
from connexionAdmin import Connexion

class Cryptage(Connexion):


    def __init__(self):
        super().__init__()



    def crypter(self, password):
    
        password = password.encode('utf-8')

        hashed = bcrypt.hashpw(password, bcrypt.gensalt())

        return hashed


    def tester_mdp(self, password, hashed):
        
        password = password.encode('utf-8')
       
        if bcrypt.checkpw(password, hashed) :
            return True
        else :
            return False

        
    def ajouter_utilisateur(self, pseudo, mdp):
        

        mdp = self.crypter(mdp).decode('utf-8')

        if self.verifier_doublon(pseudo) == False:
            self.ouvrir()
            sql = "INSERT INTO administrateurs(pseudo, motDePasse)VALUES(%s, %s);"
            val = (pseudo, mdp)
            self.cursor.execute(sql, val)
            self.conn.commit()
            self.fermer()
            return True
        else:
            return False


    def verifier_doublon(self, pseudo):
        self.ouvrir()
        self.cursor.execute("SELECT pseudo FROM administrateurs")

        liste=[]
        for i in self.cursor:
            liste.append(i[0])

        self.fermer()

        if pseudo in liste:
            return True
        else:
            return False

        
        

    def verifier_utilisateur(self, pseudo, mdp):
        self.ouvrir()
        sql = f"SELECT pseudo, motDePasse from administrateurs WHERE pseudo='{pseudo}'"
        
        try:
            self.cursor.execute(sql)
            res = [x for x in self.cursor][0]
            self.fermer()
            try:
                self.tester_mdp(mdp, res[1].encode('utf-8')) == True
                return True
            except:
                return False
        except:
            return False    
        


if __name__ =="__main__":

    cl = Cryptage()

    print(cl.ajouter_utilisateur('jame','byrne'))

    # print(cl.tester_mdp(res, 'erwan'))
    # mdp = 'voici'
    # hashed = cl.crypter(mdp)
    # print(hashed)
    # print(cl.tester_mdp('erwan', res))

    # print(cl.verifier_doublon('erwan'))