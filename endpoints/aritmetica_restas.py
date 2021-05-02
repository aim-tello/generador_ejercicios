from flask_restful import Resource
from flask import request, jsonify
from model.operaciones_request import SolicitudOperacion
from service.genera_seccion_restas_aritmeticas import GeneraRestas as gr

solicitud_operacion = SolicitudOperacion()


class RestasEndpoint(Resource):
    def post(self):
        data = request.get_json()
        solicitud_dict = solicitud_operacion.load(data)
        ejercicios_resta = gr(cantidad_restas=solicitud_dict['cantidad_restas'],
                              sumandos=solicitud_dict['sumandos'],
                              limite_superior=solicitud_dict['limite_superior'],
                              limite_inferior=solicitud_dict['limite_inferior'])
        return jsonify(ejercicios = ejercicios_resta.ejercicios_str)
