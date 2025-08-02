from flask import Flask, render_template, jsonify

app = Flask(__name__)

TEMAS = [
  {
    'ID':1,
    'Tema':'Introducción',
    'Duración':'20 min',
    'Evaluación': ' '

  },
  {
    'ID':2,
    'Tema':'Conteos',
    'Duración':'30 min',
    'Evaluación': '20%',
  },
  {
    'ID':3,
    'Tema':'Tablas',
    'Duración':'50 min',
    'Evaluación': '30%',
  },
  {
    'ID':4,
    'Tema':'Proporcionalidad',
    'Duración':'120 min',
    'Evaluación': '50%',
  },
]

@app.route("/")
def hello_pm1():
  return render_template('home.html',
                        temas=TEMAS,
                        nombre_escuela='C-205')

@app.route("/api/temas")
def list_temas():
  return jsonify(TEMAS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)