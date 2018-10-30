# app.py - Python file der WebApp
# Hier werden die verschiedenen routes bestimmt und die Datenbanke verbindung + template rendering gemacht.
#

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


@app.route("/ergebnisse")
def ergebnisse():
    args = request.args.to_dict()
    suche = args.get('q')
    result = []
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM tvseries WHERE seriesname LIKE %s"
            cursor.execute(sql, ("%"+suche+"%",))
            result = cursor.fetchall()

    finally:
        connection.close()

    return render_template("ergebnisse.html", result=result, title="Ergebnisse")


@app.route("/mehr")
def mehr():
    args = request.args.to_dict()
    SerieId = args.get("id")
    result = []
    genreList = []

    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM tvseries WHERE id = %s"
            cursor.execute(sql, (SerieId,))
            result = cursor.fetchall()

        with connection.cursor() as c:
            sql = "SELECT genres.genre FROM genres JOIN seriesgenre ON genres.id = seriesgenre.genreid JOIN tvseries ON seriesgenre.seriesid = tvseries.id  WHERE tvseries.id = %s"
            c.execute(sql, (SerieId,))
            genreList = c.fetchall()
    finally:
        connection.close()



    return render_template("mehr.html", serie=result[0], title="Mehr", genres=genreList)
