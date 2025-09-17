from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)

api = Api(app)

inv = "inventario.json"

class Hola(Resource):
    def get(self):
        return {"message": "La API esta activa"}, 200

class BuscarProducto(Resource):
    def get(self,nombre):
        output = []
        with open(inv,"r") as f:
            datos = json.load(f)
        for item in datos:
            if nombre in item["nombre"]:
                output.append(item)
        return {"encontrados": output}


class NuevoProducto(Resource):
    def post(self):
        data = request.get_json()
        nombre = data.get("nombre")
        precio = data.get("precio")
        stockInicial = data.get("stockInicial")
        with open(inv,"r") as f:
            datos = json.load(f)
        producto = {
            "nombre": nombre,
            "precio": precio,
            "Stock": stockInicial
        }
        datos.append(producto)
        with open(inv,"w") as f:
            json.dump(datos,f,indent=4,ensure_ascii=False)
        return {"message":"all good :D", "data": data},200

api.add_resource(NuevoProducto,"/NuevoProducto")
api.add_resource(BuscarProducto,"/BuscarProducto/<string:nombre>")
api.add_resource(Hola,"/")

if __name__ == "__main__":
    app.run(debug=True)