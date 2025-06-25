from app import db
class Genero(db.Model):
    __tablename__ = "generos"
    idGenero = db.column(db.Integer,primary_key=True,autoincrement=True)
    getNombre = db.column(db.String(50),nullable=False,unique=True)
    
    def __str__(self):
        return self.getNombre
