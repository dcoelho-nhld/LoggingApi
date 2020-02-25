from flask import Flask
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

from TestAPI import TestAPI

app = Flask(__name__)
api = Api(app)


# Driver Function
if __name__ == '__main__':
    api.add_resource(TestAPI, '/')
    app.run(debug=True)
    # app.run(host='0.0.0.0')
