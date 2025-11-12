from flask import Flask, request, jsonify
from time import time

app = Flask(__name__)

# Tu będą dane graczy: {nick: {x, y, z, world, last_update}}
positions = {}

@app.route("/update", methods=["POST"])
def update():
    """Gracz wysyła swoje dane: nick, pozycję i świat"""
    nick = request.form.get("nick")
    x = float(request.form.get("x"))
    y = float(request.form.get("y"))
    z = float(request.form.get("z"))
    world = request.form.get("world")
    positions[nick] = {"x": x, "y": y, "z": z, "world": world, "last": time()}
    return "OK"

@app.route("/positions")
def get_positions():
    """Zwraca wszystkich aktywnych graczy (np. ostatnie 30 sekund)"""
    now = time()
    active = {k: v for k, v in positions.items() if now - v["last"] < 30}
    return jsonify(active)

@app.route("/")
def root():
    return "Waypoint API is running!"

if __name__ == "__main__":
    # Serwer działa na porcie 5000
    app.run(host="0.0.0.0", port=5000)
