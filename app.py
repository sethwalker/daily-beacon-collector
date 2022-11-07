from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/beacon", methods=['GET', 'POST'])
def beacon():
    if (request.method == "GET"):
        return "<p>Must send data as POST</p>"

    payload = request.get_data(as_text=True)
    with open("beacon.log", "a") as f:
        f.write(payload + '\n')
    return ('', 204)
