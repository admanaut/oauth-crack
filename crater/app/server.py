from flask import Flask, request, render_template
import json

app = Flask(__name__)

clients = {
    "zMTmphvxSGGj": "Fissure"
}

@app.route('/authorize', methods=["GET"])
def authorize():
    responseType = request.args.get("response_type")
    clientId = request.args.get("client_id")
    redirectURI = request.args.get("redirect_uri")
    scope = request.args.get("scope")
    state = request.args.get("state")

    return render_template( "authorize.html",
        code=generateGrantCode(),
        client_name=clients[clientId],
        redirect_uri=redirectURI,
        state=state,
        scope=scope)

@app.route('/token', methods=["POST"])
def token():
    grantType = request.args.get("grant_type")
    code = request.args.get("code")
    clientId = request.args.get("client_id")
    clientSecret = request.args.get("client_secret")
    redirectUri = request.args.get("redirect_uri")

    data = {  'token_type': 'Bearer'
            , 'expires_in': 3600
            , 'access_token': generateAccessToken()
            , 'refresh_token': generateAccessToken()
            }

    data = json.dumps(data)
    body = str(data).encode('utf-8')

    return body

def generateGrantCode():
    return "uDwkpil@blte%&inTwRNewN6gKfCwMyo"

def generateAccessToken():
    return ""

def generateRefreshToken():
    return ""