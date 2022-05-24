from asyncore import read
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index() :
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=feac3a4822f0487ebd4dd65f081bfa16"
    r = requests.get(url).json()

    cases = {
        'articles' : r['articles']

    }

    return render_template("index.html", case = cases)

if __name__ == '__main__':
    app.run(debug=True)