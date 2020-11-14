from flask import Flask, request, send_from_directory, abort, url_for
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/protected-resource', methods=["GET"])
@cross_origin()
def authorize():
    token = request.headers.get('Authorization')

    if token:
        return "http://localhost:8082" + url_for('static', filename='holygrail.jpg')
    else:
        abort(404)