from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

user,password,host,database="root","root","localhost","peliculasDB"

cadenaConexion = f"mysql+pymysql://{user}:{password}@{host}/{database}"

app.config["SQLALCHEMY_DATABASE_URI"]=cadenaConexion

db=SQLAlchemy(app)

if __name__ == "__main__":
    from routes.pelicula import *
    from routes.genero import *
    with app.app_context():
        db.create_all()
    app.run(port=5000,debug=True)