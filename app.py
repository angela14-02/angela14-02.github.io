from flask import Flask
import subprocess
import traceback
from flask_cors import CORS  # Importar CORS

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return "Servidor Flask funcionando correctamente"

@app.route('/run-snake-test')
def run_snake_test():
    try:
        result = subprocess.run(['python3', 'snake_test.py'], capture_output=True, text=True)
        return f"<pre>{result.stdout}</pre>" if result.returncode == 0 else f"<pre>Error:\n{result.stderr}</pre>"
    except Exception as e:
        return f"<pre>Error ejecutando el archivo:\n{traceback.format_exc()}</pre>"

@app.route('/run-game')
def run_game():
    try:
        result = subprocess.run(['python3', 'game.py'], capture_output=True, text=True)
        return f"<pre>{result.stdout}</pre>" if result.returncode == 0 else f"<pre>Error:\n{result.stderr}</pre>"
    except Exception as e:
        return f"<pre>Error ejecutando el archivo:\n{traceback.format_exc()}</pre>"

@app.route('/run-memoria')
def run_memoria():
    try:
        result = subprocess.run(['python3', 'memoria.py'], capture_output=True, text=True)
        return f"<pre>{result.stdout}</pre>" if result.returncode == 0 else f"<pre>Error:\n{result.stderr}</pre>"
    except Exception as e:
        return f"<pre>Error ejecutando el archivo:\n{traceback.format_exc()}</pre>"

@app.route('/routes')
def show_routes():
    return "<br>".join([str(rule) for rule in app.url_map.iter_rules()])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
