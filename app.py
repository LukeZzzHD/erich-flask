from flask import Flask, render_template, request
import pymysql.cursors

def connect_db():
    connection = pymysql.connect(host='web3.gymkirchenfeld.ch',
                             user='thetvdb',
                             password='N08lzUvOjQpKu8Pp',
                             db='thetvdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection

imageGrid = [
    "american.jpg",
    "aot.jpg",
    "bieri.png",
    "blackmirror.jpg",
    "breakingbad.jpg",
    "carbon.jpg",
    "casa.jpg",
    "criminalminds.jpg",
    "damnation.jpg",
    "daredevil.jpg",
    "dark.jpg",
    "dead.jpg",
    "familyguy.jpg",
    "gameofthrones.jpg",
    "index.jpg",
    "logo.png",
    "lost.jpg",
    "lukecage.jpg",
    "maniac.jpg",
    "market.jpg",
    "narcos.jpg",
    "peaky.jpg",
    "prisonbreak.jpg",
    "punisher.jpg",
    "rickandmorty.jpg",
    "riverdale.jpg",
    "saul.jpg",
    "sherlock.jpg",
    "sons.jpg",
    "southpark.jpg",
    "star-rating.jpg",
    "strangerthings.jpg",
    "suits.jpg",
    "the.jpg",
    "thirteen.jpg",
    "vikings.jpg",
    "westworld.jpg",
    "whitecollar.jpg"
]

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html", title="Home")
