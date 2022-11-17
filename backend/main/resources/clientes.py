from flask_restful import Resource
from flask import jsonify, request

clientes = [
    {
"id": 1,
"nombre": "Jose",
"apellido": "Gomez"
},
{
    "id": 2,
    "nombre": "Dariana",
    "apellido": "Gomez"
}
    ]



class Clientes(Resource):
    def get(self):
        return jsonify(
            {
                "clientes": clientes
            }
        )

    def post(self):
        cliente = request.get_json()
        clientes.append(cliente)
        return cliente, 201

class Cliente(Resource):
    def get(self, id):
        return jsonify(
            {
                "Cliente": clientes[int(id)]
            }
        )