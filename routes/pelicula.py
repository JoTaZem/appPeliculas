from flask import request,render_template,jsonify
from app import app,db
from models.pelicula import *
from models.genero import *
from sqlalchemy import exc



@app.route("/peliculas", methods=["GET"])
def listarPeliculas():
    try:
        mensaje = ""
        if request.method == "GET":
            peliculas = Pelicula.query.all()
            listarPeliculas = []
            for pel in peliculas:
                listarPeliculas.append(pel.peliculaJson())
            if(len(listarPeliculas)==0):
                mensaje = "Lista de Peliculas Vacia"
            else:
                mensaje = "consula exitosa"
                     
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return jsonify({"mensaje": mensaje, "peliculas": listarPeliculas})

  
@app.route("/pelicula/crear",methods=["GET","POST"])
def crearPelicula():
    try:
        mensaje=""

        if request.method == "GET":
            return render_template("frmPelicula.html")
        else:
            datos = request.form
            if datos:
                p = Pelicula(
                    pelCodigo=datos["txtCodigo"],
                    pelTitulo=datos["txtTitulo"],
                    pelProtagonista=datos["txtProtagonista"],
                    pelDuracion=datos["txtDuracion"],
                    pelResumen=datos["txtResumen"],
                    pelFoto=datos["imgFoto"],
                    pelGenero=datos["txtGenero"])
                db.session.add(p)
                db.session.commit() 
                mensaje = "Pelicula registrada correctamente"
                return ({"mensaje": mensaje,"pelicula":p.peliculaJson()})
            else:
                mensaje="error al intentar ingresar"
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return jsonify({"mensaje": mensaje})



@app.route("/peliculas/<int:idPel>", methods=["GET"])
def listarPeliculaPorId(idPel):
    try:
        mensaje = None
        pel = None
        if request.method == "GET":
            pelicula = Pelicula.query.get(idPel)
            if pelicula:
                pel  =pelicula.peliculaJson()
                mensaje= "Consulta pelicula por id Exitosa "
                return jsonify({"mensaje":mensaje,"pelicula":pel})
            else:
                mensaje = "Pelicula no encontrada"
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
        pel = None
    return jsonify({"mensaje": mensaje, "pelicula": pel})



@app.route("/eliminar/<int:idPel>", methods=["GET"])
def eliminarPeliculaCon(idPel):
    try:
        if request.method == "GET":
            pelicula = Pelicula.query.get(idPel)
            pelEliminada=None
            if pelicula:
                pelEliminada=pelicula.peliculaJson()
                db.session.delete(pelicula)
                db.session.commit()
                mensaje = "Pelicula eliminada correctamente"
            else:
                pelEliminada={"Mensaje":f"la pelicula con el identificador # {idPel} no existe..."}
                mensaje = "La pelicula no pudo ser eliminada..."
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return jsonify({"mensaje": mensaje,"pelicula Eliminada":pelEliminada})

@app.route("/actualizar/<int:idPel>", methods=["GET"])
def actualizarPelicula(idPel): 
    try:
        datos = request.form
        pelicula = Pelicula.query.get(idPel)
        if pelicula:
            if request.method == "GET":
                return render_template("frmActualizar.html")
            else:
                #pelicula.pelCodigo = datos["pelCodigo"]
                pelicula.pelTitulo = datos["txtTitulo"]
                pelicula.pelProtagonista = datos["txtProtagonista"]
                pelicula.pelDuracion = datos["txtDuracion"]
                pelicula.pelResumen = datos["txtResumen"]
                pelicula.pelFoto = datos["txtFoto"]
                pelicula.pelGenero = datos["txtGenero"]
                db.session.commit()
                mensaje = "Pelicula actualizada correctamente"
        else:
            mensaje = "Error al actualizar: Pelicula no encontrada..."
            return jsonify({"mensaje": mensaje})
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return jsonify({"mensaje": mensaje,"pelicula":pelicula.peliculaJson()})