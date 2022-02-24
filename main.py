from flask import Flask, render_template, request
from connexion import Connexion
from requete import Requete
from traitement import Resultat


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

    return render_template('admin.html')



if __name__ == "__main__":
    app.run(debug=True)