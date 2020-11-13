from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=["GET"])
def authorize():
    return render_template("client.html",
        step="begin",
        client_id="zMTmphvxSGGj",
        state="6JgnSxWzv5Xd",
        return_uri=url_for('receiveGrantCode'))

@app.route('/receive-grant-code', methods=["GET"])
def receiveGrantCode():
    return "OK"