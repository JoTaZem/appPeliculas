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
        if(len(listarGeneros)==0):
            mensaje = "Lista de Generos Vacia"
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return jsonify({"mensaje":mensaje, "generos": listarGeneros}) 

@app.route("/generos/<int:idGen>", methods=["GET"])
def listarGeneroPorId(idGen):
    mensaje = "Consulta exitosa"
    gen = None
    try:
        gen = Genero.query.get(idGen)
        if gen:
            genero = {
                "idGenero": gen.idGenero,
                "genNombre": gen.genNombre
            }
        else:
            mensaje = "Genero no encontrado"
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return jsonify({"mensaje": mensaje, "genero": genero if gen else None})

@app.route("/generos", methods=["POST"])
def registrarGenero(): 
    mensaje = "Registro exitoso"
    try:
        datos = request.get_json()
        gen = Genero(
            genNombre=datos["genNombre"]
        )
        db.session.add(gen)
        db.session.commit()
        return jsonify({"mensaje": mensaje, "id de genero": gen.idGenero})
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return jsonify({"mensaje": mensaje})

@app.route("/generos/<int:idGen>", methods=["PUT"])
def actualizarGenero(idGen):
    mensaje = "Actualizacion exitosa"
    try:
        gen = Genero.query.get(idGen)
        if gen:
            datos = request.get_json()
            gen.genNombre = datos["genNombre"]
            db.session.commit()
        else:
            mensaje = "Genero no encontrado"
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return jsonify({"mensaje": mensaje})

@app.route("/generos/<int:idGen>", methods=["DELETE"])
def eliminarGenero(idGen):
    mensaje = "Eliminacion exitosa"
    try:
        gen = Genero.query.get(idGen)
        if gen:
            db.session.delete(gen)
            db.session.commit()
        else:
            mensaje = "Genero no encontrado"
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return jsonify({"mensaje": mensaje})