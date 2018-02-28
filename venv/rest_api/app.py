from flask import Flask
import flask.ext.restful as rest

app = Flask(__name__)
api = rest.Api(app)

if __name__ == '__main__':
    app.run(debug=True)