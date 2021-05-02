from config.exports import ma
from marshmallow import fields


class SolicitudOperacion(ma.Schema):
    cantidad_restas = fields.Integer(required=True)
    sumandos = fields.Integer(required=True)
    limite_superior = fields.Integer(required=True)
    limite_inferior = fields.Integer(required=True)
