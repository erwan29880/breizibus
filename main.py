from flask import Flask, render_template, request
from connexion import Connexion
from requete import Requete



app = Flask(__name__)




@app.route('/', methods = ['GET','POST'])
def home():
    
    affichage = 0
    retour_req=None

    # incrémentation du diaporama
    if request.form:
        # res = request.form
        co = Connexion()
        retour_req = co.req()
        affichage=1

    return render_template('index.html', res1=retour_req, verif=affichage)




if __name__ == "__main__":
    app.run(debug=True)