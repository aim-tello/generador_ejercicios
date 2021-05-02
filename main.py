from flask import Flask
from flask_restful import Api
from endpoints.aritmetica_restas import RestasEndpoint
import config.manejo_errores as me

app = Flask(__name__)
api = Api(app)
#me.register_error_handlers(app)

api.add_resource(RestasEndpoint, '/hola')


@app.route("/")
def index():
    return 'app Viva!'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
