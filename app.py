from flask import Flask, render_template, jsonify

app = Flask(__name__)


TEMAS = [
  {
    'id':1,
    'pg': 'Progresión 1',
    'Tema':'Introducción',
    'Duración':'20 min',
    'Evaluación': ' ',
    'Contenido': 'Hola, bienvenido a la clase de Pensamiento Matemático I. En esta clase aprenderemos a resolver problemas de manera intuitiva con base en el razonamiento lógico.',
    'Apertura': 'Para comenzar la clase, vamos a resolver un problema rescatando conocimientos previos.',
    'Caso': 'En un grupo de 10 personas, 3 personas son mujeres y 7 son hombres, ¿cuántas personas hay en total y cuántas son mujeres?',
    'Desarrollo': 'Con las técnicas y las herramientas que ya vimos anteriormente, ahora buscaremos resolver situaciones diferentes.',
    'Resuelve': 'Para resolver este problema primero contamos el total de personas y luego identificamos en la lectura cuántas son mujeres?',
    'Cierre': 'Con la finalidad de tener retroalimentación acerca de los temas anteriormente cubiertos, realizaremos una actividad final antes de continuar con el programa.'
  },
  
  {
    'id':2,
    'pg': 'Progresión 2',
    'Tema':'Conteos',
    'Duración':'30 min',
    'Evaluación': '20%',
    'Contenido': 'En esta clase aprenderemos algunas técnicas útiles para contar objetos.',
    'Apertura': 'Para comenzar la clase, vamos a resolver un problema rescatando conocimientos previos.',
    'Caso': 'En un aparador de una tienda de teléfonos celulares hay 3 marcas diferentes. De la primera marca hay 5 modelos, de la segunda marca hay 4 modelos y de la tercera marca hay 6 modelos. ¿Cuántos modelos de teléfonos celulares hay en total?',
    'Desarrollo': 'Con las técnicas y las herramientas que ya vimos anteriormente, ahora buscaremos resolver situaciones diferentes.',
    'Resuelve': 'Para resolver este problema primero contamos los modelos de cada marca y luego sumamos para obtener el total',
    'Cierre': 'Con la finalidad de tener retroalimentación acerca de los temas anteriormente cubiertos, realizaremos una actividad final antes de continuar con el programa.'
  },
  
  {
    'id':3,
    'pg': 'Progresión 3',
    'Tema':'Tablas',
    'Duración':'50 min',
    'Evaluación': '30%',
    'Contenido': 'Las tablas son una herramienta útil para organizar información y resolver problemas.',
    'Apertura': 'Para comenzar la clase, vamos a resolver un problema rescatando conocimientos previos.',
    'Caso': '¿Recuerdas las marcas de teléfonos celulares que contamos en la clase anterior? Ahora vamos a organizar la información en una tabla.',
    'Desarrollo': 'Con las técnicas y las herramientas que ya vimos anteriormente, ahora buscaremos resolver situaciones diferentes.',
    'Resuelve': 'Con ayuda de tu ptofesor en clase, organiza la información de los teléfonos celulares en una tabla. Recuerda que una tabla debe tener enccabezados y su estructura consiste en filas y columnas. No olvides además incluir un título en la parte superior de la tabla. El título debe ser breve y claro y debe indicar el contenido de la tabla.',
    'Cierre': 'Con la finalidad de tener retroalimentación acerca de los temas anteriormente cubiertos, realizaremos una actividad final antes de continuar con el programa.'
  },
  {
    'id':4,
    'pg': 'Progresión 4',
    'Tema':'Proporcionalidad',
    'Duración':'120 min',
    'Evaluación': '50%',
    'Contenido': 'En esta clase aprenderemos a resolver problemas que involucran relaciones entre cantidades.',
    'Apertura': 'Para comenzar la clase, vamos a resolver un problema rescatando conocimientos previos.',
    'Caso': 'En un grupo de 10 personas, 3 personas son hombres y 7 son mujeres, ¿Cuál es la proporción de hombres y mujeres?',
    'Desarrollo': 'Con las técnicas y las herramientas que ya vimos anteriormente, ahora buscaremos resolver situaciones diferentes.',
    'Resuelve': 'Para resolver este problema primero contamos el total de personas que hay en el grupo y luego identificamos cuántas son hombres y cuántas son mujeres. Finalmente, dividimos el número de hombres entre el total de personas para obtener la proporción de hombres; hacemos el mismo procedimiento para obtener la proporción de mujeres.',
    'Cierre': 'Con la finalidad de tener retroalimentación acerca de los temas anteriormente cubiertos, realizaremos una actividad final para entregar antes de continuar con el programa.'
  },
]

@app.route("/")
def hello_pm1():
  return render_template('home.html',
                        temas=TEMAS
                        )





@app.route('/tema/<int:tema_id>')
def show_tema(tema_id):
    # Supongamos que TEMAS es tu estructura de datos (lista o dict)
    tema = TEMAS[tema_id-1]
    return render_template('classpage.html', i=tema)
  

@app.route("/api/temas")
def list_temas():
  return jsonify(TEMAS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)