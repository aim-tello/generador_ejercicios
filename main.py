from flask import Flask
from flask_restful import Api
from endpoints.aritmetica_restas import RestasEndpoint
import config.manejo_errores as me
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)
me.register_error_handlers(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

api.add_resource(RestasEndpoint, '/hola')


@app.route("/")
def index():
    return 'app Viva!'


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
