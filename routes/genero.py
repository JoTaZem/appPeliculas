from flask import request,render_template
from app import app,db
from models.genero import *
from sqlalchemy import exc

@app.route("/generos", methods=["GET"])
def listarGeneros():
    try:
        mensaje = None
        generos = Genero.query.all()
        listarGeneros=[]
        for gen in generos:
            genero={
                "idGenero": gen.idGenero,
                "genNombre": gen.getNombre
            }
            listarGeneros.append(genero)
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return {"mensaje":mensaje, "generos": listarGeneros}
