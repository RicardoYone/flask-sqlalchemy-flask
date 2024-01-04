from app import db
from sqlalchemy import func


class AlumnoModel(db.Model):
    alumnoId = db.Column(db.Integer, primary_key=True)
    alumnoNombre = db.Column(db.String(100), nullable=False)
    alumnoDni = db.Column(db.String(8), nullable=False)
    alumnoEdad = db.Column(db.Integer, nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now())

    def __str__(self) -> str:
        return f'{self.alumnoNombre}'

    def __init__(self, nombre, dni, edad) -> None:
        self.alumnoNombre = nombre
        self.alumnoDni = dni
        self.alumnoEdad = edad

    def json(self):
        return {
            "alumnoId": self.alumnoId,
            "alumnoNombre": self.alumnoNombre,
            "alumnoDni": self.alumnoDni,
            "alumnoEdad": self.alumnoEdad
        }

    def guardar_db(self):
        db.session.add(self)
        db.session.commit()
        return self.json()

    def actualizar_db(self, nombre=None, dni=None, edad=None):
        if nombre:
            self.alumnoNombre = nombre
        if dni:
            self.alumnoDni = dni
        if edad:
            self.alumnoEdad = edad
        db.session.commit()
        return self.json()

    def eliminar_db(self):
        db.session.delete(self)
        db.session.commit()
        return self.json()
