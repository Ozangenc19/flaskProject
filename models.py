from . import app, db

from flask_sqlalchemy import SQLAlchemy


class vue_produits_categories(db.Model):
    id_produit = db.Column(db.Integer, primary_key=True)
    nom_produit = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    prix_produit = db.Column(db.Float(10), nullable=True)
    nom_categorie = db.Column(db.String(30), nullable=False)
    image_produit = db.Column(db.String(30), nullable=True, default='default.jpg')
    image_cat = db.Column(db.String(30), nullable=True, default='default.jpg')
    id_cat = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id_produit} : {self.nom_produit} : {self.description} : {self.prix_produit} : {self.image_produit}: {self.image_cat}: {self.nom_categorie} : {self.id_cat}'


class vue_creation(db.Model):
    id_creation = db.Column(db.Integer, primary_key=True);
    nom_creation = db.Column(db.String(25), nullable=False);
    description = db.Column(db.String(200), nullable=True);
    prix_creation = db.Column(db.Float(10), nullable=True);
    image_creation = db.Column(db.String(30), nullable=True, default='default.jpg');

    def __repr__(self):
        return f'{self.id_creation} : {self.nom_creation} : {self.description} : {self.prix_creation} : {self.image_creation}'


class vue_nouveaute(db.Model):
    id_nouveaute = db.Column(db.Integer, primary_key=True);
    nom_nouveaute = db.Column(db.String(25), nullable=False);
    description = db.Column(db.String(200), nullable=True);
    prix_nouveaute = db.Column(db.Float(10), nullable=True);
    image_nouveaute = db.Column(db.String(30), nullable=True, default='default.jpg');

    def __repr__(self):
        return f'{self.id_nouveaute} : {self.nom_nouveaute} : {self.description} : {self.prix_nouveaute} : {self.image_nouveaute}'
