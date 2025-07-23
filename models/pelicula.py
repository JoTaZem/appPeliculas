from app import db
class Pelicula(db.Model):
    
    __tablename__ = "peliculas"
    
    idPelicula = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pelCodigo = db.Column(db.String(9), nullable=False, unique=True)
    pelTitulo = db.Column(db.String(100), nullable=False)
    pelProtagonista = db.Column(db.String(50), nullable=False)
    pelDuracion = db.Column(db.Integer,nullable=False)
    pelResumen = db.Column(db.Text,nullable=False)
    pelFoto = db.Column(db.String(45))
    pelGenero = db.Column(db.Integer, db.ForeignKey("generos.idGenero"), nullable=False)
    genero = db.relationship("Genero", backref = "peliculas",lazy=True)    
    
    def __str__(self):
        return self.pelTitulo
    
    def peliculaJson(self):
        return{"idPelicula": self.idPelicula,
                    "pelCodigo": self.pelCodigo,
                    "pelTitulo": self.pelTitulo,
                    "pelProtagonista": self.pelProtagonista,
                    "pelDuracion": self.pelDuracion, 
                    "pelResumen": self.pelResumen,
                    "pelFoto": self.pelFoto,
                    "pelGenero": {"idGenero":self.genero.idGenero,"genNombre":self.genero.genNombre}}