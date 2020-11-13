from flask import Flask
from flask import request
from flask import render_template

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

    grantCode = generateGrantCode()

    return render_template( "authorize.html",
        code=grantCode,
        client_name=clients[clientId],
        redirect_uri=redirectURI,
        state=state,
        scope=scope)

def generateGrantCode():
    return "uDwkpil@blte%&inTwRNewN6gKfCwMyo"

def generateAuthCode():
    return "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXNzYWdlIjoiSldUIFJ1bGVzISIsImlhdCI6MTQ1OTQ0ODExOSwiZXhwIjoxNDU5NDU0NTE5fQ.-yIVBD5b73C75osbmwwshQNRC7frWUYrqaTjTpza2y4"