from flask import Flask, request, render_template, redirect, url_for, jsonify
import os
import requests
from db import (
    init_db,
    create_person,
    get_people,
    update_person,
    delete_person
)

app = Flask(__name__)
init_db()

AWS_PEER = os.getenv("AWS_OTHER_HOST")
AZURE_PEER = os.getenv("AZURE_OTHER_HOST")

# 👉 IDENTIFICAR NUBE ACTUAL
def get_current_cloud():
    if AZURE_PEER:
        return "AWS"
    if AWS_PEER:
        return "Azure"
    return "Desconocida"

# 👉 REPLICACIÓN
def replicate(endpoint, payload):
    for peer in [AWS_PEER, AZURE_PEER]:
        if peer:
            try:
                requests.post(
                    f"http://{peer}:49154{endpoint}",
                    json=payload,
                    timeout=2
                )
            except Exception as e:
                print("Error replicando:", e)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = dict(request.form)
        create_person(data)
        replicate("/replica/create", data)
        return redirect(url_for("index"))

    return render_template(
        "index.html",
        people=get_people(),
        cloud=get_current_cloud()
    )

@app.route("/update/<int:pid>", methods=["POST"])
def update(pid):
    data = dict(request.form)
    update_person(pid, data)
    replicate("/replica/update", {"id": pid, **data})
    return redirect(url_for("index"))

@app.route("/delete/<int:pid>", methods=["POST"])
def delete(pid):
    delete_person(pid)
    replicate("/replica/delete", {"id": pid})
    return redirect(url_for("index"))

# ===== ENDPOINTS DE RÉPLICA =====

@app.route("/replica/create", methods=["POST"])
def replica_create():
    create_person(request.json)
    return jsonify({"status": "ok"})

@app.route("/replica/update", methods=["POST"])
def replica_update():
    data = request.json
    update_person(data["id"], data)
    return jsonify({"status": "ok"})

@app.route("/replica/delete", methods=["POST"])
def replica_delete():
    delete_person(request.json["id"])
    return jsonify({"status": "ok"})

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
