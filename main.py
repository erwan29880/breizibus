from flask import Flask, render_template, request
from connexion import Connexion
from requete import Requete
from admin import Administration
from mdp import Cryptage
from traitement import Cookie


app = Flask(__name__)




@app.route('/', methods = ['GET','POST'])
def home():
    
    # selon que l'on affiche les résultats en front ou non --> 0 --> non
    affichage = 0
    retour_req=None
    texte = None

    affichage_initial = Requete().requete_ligne()

    # récupération des données du formulaire
    if request.form:
        res = request.form['lignes']
        
        retour_req = Requete().voir_arrets(res)[0]
        texte = Requete().voir_arrets(res)[1] 
        
                    
        affichage=1

    return render_template('index.html', aff=affichage_initial, res1=retour_req, texte=texte, verif=affichage)



@app.route('/admin', methods = ['GET','POST'])
def admin():

    cook = Cookie()
    utilisateur = Cryptage()


    if request.form:
        if request.form['verification']=='50':
            res = request.form
            if Cryptage().verifier_utilisateur(res['pseudo'], res['password']) == True:
                cook.set_cookie()
            
        if request.form['verification']=='200':
                cook.unset_cookie()


    if cook.read_cookie[0] == '1':

        varGlobale = 1
        affichage_initial = Requete().requete_ligne()
        affichage_suppression = Administration().voir_bus2()
        retour_arret=None
        retour_bus=None
        texte = None
        var = 0



        if request.form:

            if request.form['verification']=='2':
                res=request.form

                # enregsitrer une nouvelle entrée
                Administration().commit(res['immat'],res['places'], res['adminLigne'])
                var = 1


            if request.form['verification']=='3':
                
                res = request.form['ligneAdmin']
                retour_arret = Requete().voir_arrets(res)[0]
                texte = Requete().voir_arrets(res)[1]           
                retour_bus = Administration().voir_bus(res)
                var = 2


            if request.form['verification']=='4':
                
                res = request.form['supp']
                Administration().supprimer_bus(res)
                var = 3
            

            if request.form['verification']=='5':
                
                res = request.form
                Administration().update(res['supp'],res['ligneAdmin'],res['immat'],res['places'])
                var = 4

            


        return render_template('admin.html', varGlobale=varGlobale,aff=affichage_initial, var=var, res1=retour_arret, texte=texte, bus=retour_bus, suppression=affichage_suppression )

    else:
        varGlobale=0
        return render_template('admin.html', varGlobale=varGlobale)



@app.route('/connexion', methods = ['GET','POST'])
def connexion():

    return render_template('connexion.html')



@app.route('/enregistrement', methods = ['GET','POST'])
def enregistrement():
    var = 0

    if request.form:
        if request.form['verification']=='11':
            res = request.form
            cl = Cryptage()
            res = cl.ajouter_utilisateur(res['pseudo'], res['password'])
            if res==True:
                var=1
            else:
                var=2

    return render_template('enregistrement.html', var=var)





if __name__ == "__main__":
    app.run(debug=True)