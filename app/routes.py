from app import app
from flask import render_template, jsonify
from app.bobagame import game

@app.route("/")
def index():
    game.basicButtonCounter = 0 #reset score on reload
    return render_template("index.html", count=game.get_count())

@app.route("/increment", methods=["POST"])
def increment():
    new_count = game.increment()
    return jsonify({"count": new_count})