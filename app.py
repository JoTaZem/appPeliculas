from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
load_dotenv()

app= Flask(__name__)

cadenaConexion = os.environ.get("URI")

app.config["SQLALCHEMY_DATABASE_URI"]=cadenaConexion

db=SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    from routes.genero import *
    from routes.pelicula import *
    with app.app_context():
        db.create_all()
    app.run(port=5000,debug=True)