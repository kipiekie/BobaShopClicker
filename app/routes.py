from app import app
from flask import render_template, jsonify
from app.bobagame import game

@app.route("/")
def index():
    game.basicButtonCounter = 0 #reset score on reload
    game.buttonUpgrades["ten"] = False  # reset upgrade on reload
    return render_template(
        "index.html", 
        count=game.get_count(),
        upgrade_unlocked=game.buttonUpgrades["ten"]
    )

@app.route("/increment", methods=["POST"])
def increment():
    new_count = game.increment()
    return jsonify({
        "count": new_count,
        "upgrade_unlocked": game.buttonUpgrades["ten"]
    })

@app.route("/basic_button_upgrade", methods=["POST"])
def basic_button_upgrade():
    success = game.basicButtonUpgrade()
    return jsonify({
        "success": success,
        "count": game.get_count(),
        "upgrade_unlocked": game.buttonUpgrades["ten"]
    })