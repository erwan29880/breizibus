from flask import Flask, render_template, request
from connexion import Connexion
from requete import Requete
from traitement import Resultat
from admin import Administration

app = Flask(__name__)




@app.route('/', methods = ['GET','POST'])
def home():
    
    # selon que l'on affiche les résultats en front ou non --> 0 --> non
    affichage = 0
    retour_req=None
    texte = None

    affichage_initial = Resultat().formulaire()

    # récupération des données du formulaire
    if request.form:
        res = request.form['lignes']
        
        retour_req = Resultat().traitement(res)[0]
        texte = Resultat().traitement(res)[1] 
        
                    
        affichage=1

    return render_template('index.html', aff=affichage_initial, res1=retour_req, texte=texte, verif=affichage)






@app.route('/admin', methods = ['GET','POST'])
def admin():

    affichage_initial = Resultat().formulaire()
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
                    
            retour_arret = Resultat().traitement(res)[0]
            texte = Resultat().traitement(res)[1] 
            
            retour_bus = Administration().voir_bus(res)
                
            var = 2


        


    return render_template('admin.html',aff=affichage_initial, var=var, res1=retour_arret, texte=texte, bus=retour_bus)



if __name__ == "__main__":
    app.run(debug=True)