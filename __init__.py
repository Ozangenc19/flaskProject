from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#clé secrète générée dans la console Python de Pycharm
app.config['SECRET_KEY'] = '51a09b203f205a2a9fc8f042f6452795'
#supprime les notifications inutiles
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#configuration de la base de données
app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://anonyme:anonyme@localhost/postgres'

db = SQLAlchemy(app)


from . import routes
