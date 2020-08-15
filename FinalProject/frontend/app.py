try:
    from flask import Flask
    from flask import request,redirect,render_template,session
    import requests
    import base64
    import requests
except Exception as e:
    print('Error : {} '.format(e))

app = Flask(__name__)

global DOMAIN
DOMAIN = "http://ec2-34-232-80-5.compute-1.amazonaws.com:5000"

@app.route('/shopping', methods=["GET", "POST"])
def index():
    return render_template("home.html")


@app.route('/', methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route('/search', methods=["GET", "POST"])
def search():
    what = request.form.get("what")
    url = DOMAIN + "/search?what="+what
    r = requests.get(url)
    r = r.json()
    return r


@app.route('/pipe', methods=["GET", "POST"])
def pipe():
    data = request.form.get("data")
    payload = {}
    headers= {}
    url = DOMAIN + "/autocomplete?what="+str(data)
    response = requests.request("GET", url, headers=headers, data = payload)
    return response.json()



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
