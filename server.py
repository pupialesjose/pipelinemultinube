from flask import Flask, request, render_template, jsonify
import os
import requests
from db import init_db, save_note, get_notes

app = Flask(__name__)
init_db()

AWS_PEER = os.getenv("AWS_OTHER_HOST")
AZURE_PEER = os.getenv("AZURE_OTHER_HOST")

def replicate(note):
    for peer in [AWS_PEER, AZURE_PEER]:
        if peer:
            try:
                requests.post(
                    f"http://{peer}:8080/replica",
                    json={"content": note},
                    timeout=2
                )
            except:
                pass  # Si la otra nube cae, no rompemos nada

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form["note"]
        save_note(note)
        replicate(note)
    return render_template("index.html", notes=get_notes())

@app.route("/replica", methods=["POST"])
def replica():
    data = request.get_json()
    save_note(data["content"])
    return jsonify({"status": "replicated"})

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
