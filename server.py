from flask import Flask, request, render_template, redirect, url_for, jsonify
import os, requests
from db import *

app = Flask(__name__)
init_db()

AWS_PEER = os.getenv("AWS_OTHER_HOST")
AZURE_PEER = os.getenv("AZURE_OTHER_HOST")

def peers():
    return [p for p in [AWS_PEER, AZURE_PEER] if p]

def replicate(endpoint, payload):
    for peer in peers():
        try:
            requests.post(f"http://{peer}:49154{endpoint}", json=payload, timeout=2)
        except:
            pass

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = dict(request.form)
        note_id = create_note(data)
        data["id"] = note_id
        replicate("/replica/create", data)
        return redirect(url_for("index"))

    return render_template("index.html", notes=get_notes())

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    data = dict(request.form)
    update_note(id, data)
    data["id"] = id
    replicate("/replica/update", data)
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    delete_note(id)
    replicate("/replica/delete", {"id": id})
    return redirect(url_for("index"))

# ===================== REPLICAS =====================

@app.route("/replica/create", methods=["POST"])
def replica_create():
    data = request.json
    create_note(data)
    return jsonify(ok=True)

@app.route("/replica/update", methods=["POST"])
def replica_update():
    data = request.json
    update_note(data["id"], data)
    return jsonify(ok=True)

@app.route("/replica/delete", methods=["POST"])
def replica_delete():
    delete_note(request.json["id"])
    return jsonify(ok=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
