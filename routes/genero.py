from flask import request,render_template
from app import app,db
from models.genero import Genero
from sqlalchemy import exc
