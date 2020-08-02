from flask import Flask
from flask import request,redirect,render_template,session
import requests
import base64
import requests

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("home.html")


@app.route('/pipe', methods=["GET", "POST"])
def pipe():

    UserId = request.form.get("UserId")
    ItemId =  request.form.get("ItemId")

    import requests
    url = "http://localhost:8000/recommendation?userId={}&itemID={}".format(UserId,ItemId)
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))

    return response.json()


if __name__ == "__main__":
    app.run(debug=True, port=5000)