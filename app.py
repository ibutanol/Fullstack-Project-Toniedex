from flask import Flask, render_template
import requests



app = Flask(__name__)


@app.route("/tonies")
def get_tonies():
    response = requests.get("http://127.0.0.1:8888/tonies")
    Jsondic = response.json()
    return render_template("Tonies.html", Jsondic=Jsondic)


@app.route('/tonie/<int:tonie_id>')
def get_tonie(tonie_id):
    response = requests.get(f"http://127.0.0.1:8888/tonie/{tonie_id}")
    Jsondic = response.json()
    return render_template("Tonie.html", Jsondic=Jsondic)

if __name__ == '__main__':
    app.run(debug=True)