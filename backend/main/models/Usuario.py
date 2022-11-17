from .. import db
import datetime as dt

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True, index=True)
    role = db.Column(db.String(45), nullable=False, default="Cliente")
    telefono = db.Column(db.Integer, nullable=False)
    fecha_registro = db.Column(db.DateTime, default=dt.datetime.now(), nullable=False)


    def __repr__(self):
        return f'{self.nombre}'

    def to_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono,
            'role': self.role,
            'fecha': str(self.fecha_registro)
        }
        return usuario_json


    @staticmethod
    def from_json(usuario_json):
        id = usuario_json.ger('id')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        email = usuario_json.get('email')
        telefono = usuario_json.get('telefono')
        role = usuario_json.get('role')
        fecha_registro = usuario_json.get('fecha')
        return Usuario(
            id = id,
            nombre = nombre,
            apellido = apellido,
            email = email,
            telefono = telefono,
            role = role,
            fecha_registro = fecha_registro
        )