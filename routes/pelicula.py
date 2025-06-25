from flask import request,render_template
from app import app,db
from models.pelicula import *
from sqlalchemy import exc
@app.route("/peliculas", methods=["GET"])
def listarPeliculas():
    try:
        mensaje = None
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
                "pelGenero": pel.pelGenero
            }
            listarPeliculas.append(pelicula)
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return {"mensaje": mensaje, "peliculas": listarPeliculas}