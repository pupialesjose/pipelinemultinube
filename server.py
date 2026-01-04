from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Lista en memoria para almacenar notas
notes = []

@app.route('/')
def index():
    with open("index.html") as f:
        return f.read()

@app.route('/notes', methods=['GET', 'POST'])
def manage_notes():
    if request.method == 'POST':
        note = request.json.get("note")
        if note:
            notes.append(note)
        return jsonify(notes)
    else:
        return jsonify(notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
