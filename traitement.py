import os


class Cookie:


    def __init__(self):
        self.dossier = os.getcwd()
        self.fichier = os.path.join(self.dossier, 'cook.txt')
        self.lister_fichiers = os.listdir(self.dossier)


    def verifier_fichier(self):
        
        if self.fichier in self.lister_fichiers:
            return True
        else:
            return False
        

    def set_cookie(self):
        f = open(self.fichier, 'w')
        f.write('1')
        f.close()
        

    @property
    def read_cookie(self):
        f = open(self.fichier, 'r')
        res = f.read()
        f.close()
        return res


    def unset_cookie(self):
        f = open(self.fichier, 'w')
        f.write('0')
        f.close()

    

if __name__ =="__main__":

    cl = Cookie()

    cl.unset_cookie()
    cl.set_cookie()
    print(cl.read_cookie)





