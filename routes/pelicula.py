from flask import request,render_template
from app import app,db
from models.pelicula import Pelicula
from sqlalchemy import exc
