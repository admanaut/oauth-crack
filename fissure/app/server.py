from flask import Flask, request, render_template, url_for
import urllib
import json

app = Flask(__name__)

clientId = "zMTmphvxSGGj"

@app.route('/', methods=["GET"])
def authorize():
    return render_template("client.html",
        step="begin",
        client_id=clientId,
        state="6JgnSxWzv5Xd",
        return_uri=url_for('receiveGrantCode'))

@app.route('/receive-grant-code', methods=["GET"])
def receiveGrantCode():
    # 1. get Grant token
    grantCode = request.args.get("code")
    state = request.args.get("state")

    data = {  'grant_type': 'authorisation_code'
            , 'code': grantCode
            , 'client_id': clientId
            , 'client_secret': ''
            , 'redirect_uri': ''
            }

    body = json.dumps(data).encode('utf-8')

    # 2. exchange it for access token
    req =  urllib.request.Request("http://localhost:8080/token", data=body)
    resp = urllib.request.urlopen(req)

    respData = json.loads(resp.read().decode('utf-8'))

    # tokenType = respData['token_type']
    # accessToken = respData['access_token']
    # refreshToken = respData['refresh_token']
    # expiresIn = respData['expires_in']

    return render_template("client.html",
        step="begin",
        client_id=clientId,
        state="6JgnSxWzv5Xd",
        return_uri=url_for('receiveGrantCode'),

        auth=respData)
