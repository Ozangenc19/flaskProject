from flask import render_template, url_for, request  # on importe ce module appartenant ("from") au package flask

from . import app, models


@app.route('/')
@app.route('/accueil')
def accueil():
    liste_categories = models.vue_produits_categories.query.distinct('nom_categorie')
    return render_template('accueil.html',
                           title='Bienvenue dans notre boutique', liste=type(liste_categories),
                           liste_cat=liste_categories
                           )


@app.route('/tous_produits')
def produits():
    liste_produits = models.vue_produits_categories.query.all()
    return render_template('tous_produits.html', title='Vêtements', liste_prod=liste_produits)


@app.route('/creation')
def creations():
    liste_creations = models.vue_creation.query.all()
    return render_template('creation.html', title='Creations', liste_crea=liste_creations)


@app.route('/nouveaute')
def nouveautes():
    liste_nouveaute = models.vue_nouveaute.query.all()
    return render_template('nouveaute.html', title='Nouveautés', liste_nouv=liste_nouveaute)


