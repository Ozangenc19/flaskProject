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
    return render_template('tous_produits.html', title='Easy Clothes', liste_prod=liste_produits)


@app.route('/produits_categorie')
def produits_categorie():
    id_cat = request.args.get('id_cat')
    liste_produits = models.vue_produits_categories.query.filter_by(id_cat=id_cat)
    return render_template('produits_categorie.html', title='Easy Clothes', produits=liste_produits,
                           typeprod=type(liste_produits))

@app.route('/creation')
def creations():
    liste_creations = models.vue_creation.query.all()
    return render_template('creation.html', title='Easy Clothes', liste_crea=liste_creations)
@app.route('/nouveaute')
def nouveautes():
    liste_nouveaute = models.vue_nouveaute.query.all()
    return render_template('nouveaute.html', title='Easy Clothes', liste_nouv=liste_nouveaute)