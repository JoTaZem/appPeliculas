from flask import request,render_template,jsonify
from app import app,db
from models.pelicula import *
from models.genero import *
from sqlalchemy import exc
@app.route("/peliculas", methods=["GET", "POST"])
def listarPeliculas():
    try:
        mensaje = None
        if request.method == "GET":
            peliculas = Pelicula.query.all()
            listarPeliculas = []
            for pel in peliculas:
                pelicula = { 
                    "idPelicula": pel.idPelicula,
                    "pelCodigo": pel.pelCodigo,
                    "pelTitulo": pel.pelTitulo,
                    "pelProtagonista": pel.pelProtagonista,
                    "pelDuracion": pel.pelDuracion, 
                    "pelResumen": pel.pelResumen,
                    "pelFoto": pel.pelFoto,
                    "pelGenero": {"idGenero":pel.genero.idGenero,"genNombre":pel.genero.genNombre}
                }
                listarPeliculas.append(pelicula)
            else:
                mensaje="pelicula no permitida"

        elif request.method == "POST":
            datos = request.get_json()
            print(datos)
            p = Pelicula(
                pelCodigo=datos["pelCodigo"],
                pelTitulo=datos["pelTitulo"],
                pelProtagonista=datos["pelProtagonista"],
                pelDuracion=datos["pelDuracion"],
                pelResumen=datos["pelResumen"],
                pelFoto=datos["pelFoto"],
                idGenero=datos["idGenero"])
            db.session.add(p)
            db.session.commit() 
            mensaje = "Pelicula registrada correctamente"
            return jsonify({"mensaje": mensaje, "id de pelicula": p.idPelicula})

    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return jsonify({"mensaje": mensaje, "peliculas": listarPeliculas})
 


@app.route("/peliculas/<int:idPel>", methods=["GET"])
def listarPeliculaPorId(idPel):
    try:
        mensaje = None
        pel = None
        if request.method == "GET":
            pelicula = Pelicula.query.get(idPel)
            if pelicula:
                pel  = {
                    "idPelicula": pelicula.idPelicula,
                    "pelCodigo": pelicula.pelCodigo,
                    "pelTitulo": pelicula.pelTitulo,
                    "pelProtagonista": pelicula.pelProtagonista,
                    "pelDuracion": pelicula.pelDuracion,
                    "pelResumen": pelicula.pelResumen,
                    "pelFoto": pelicula.pelFoto,
                    "pelGenero": {"idGenero": pelicula.genero.idGenero, "genNombre": pelicula.genero.genNombre}
                }
            else:
                mensaje = "Pelicula no encontrada"
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
        pel = None
    return jsonify({"mensaje": mensaje, "pelicula": pel})
  
  
  @app.route("/eliminarPelicula/<int:idPel>", methods=["DELETE"])
  def eliminarPeliculaCon(idPel):
    try:
        if request.method == "DELETE":
            if pelicula= Pelicula.query.get(idPel):
                db.session.delete(pelicula)
                db.session.commit()
                mensaje = "Pelicula eliminada correctamente"
            else:
                mensaje = "Pelicula no encontrada"
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return jsonify({"mensaje": mensaje})