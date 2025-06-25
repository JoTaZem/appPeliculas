from flask import request,render_template,jsonify
from app import app,db
from models.genero import Genero
from sqlalchemy import exc

@app.route("/generos", methods=["GET"])
def listarGeneros():
    mensaje = "Consulta exitosa"
    try:
        generos = Genero.query.all()
        listarGeneros=[]
        for gen in generos:
            genero={
                "idGenero": gen.idGenero,
                "genNombre": gen.genNombre
            }
            listarGeneros.append(genero)
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return jsonify({"mensaje":mensaje, "generos": listarGeneros}) 


