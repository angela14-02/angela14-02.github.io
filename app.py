from flask import Flask
import subprocess

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Ruta para ejecutar snake_test.py
@app.route('/run-snake-test')
def run_snake_test():
    try:
        # Ejecutar el archivo de Python
        result = subprocess.run(['python3', 'snake_test.py'], capture_output=True, text=True)
        # Devolver el resultado o error si ocurrió
        return f"<pre>{result.stdout}</pre>" if result.returncode == 0 else f"<pre>Error:\n{result.stderr}</pre>"
    except Exception as e:
        return f"<pre>Error ejecutando el archivo:\n{e}</pre>"

# Ruta para ejecutar game.py
@app.route('/run-game')
def run_game():
    try:
        # Ejecutar el archivo de Python
        result = subprocess.run(['python3', 'game.py'], capture_output=True, text=True)
        # Devolver el resultado o error si ocurrió
        return f"<pre>{result.stdout}</pre>" if result.returncode == 0 else f"<pre>Error:\n{result.stderr}</pre>"
    except Exception as e:
        return f"<pre>Error ejecutando el archivo:\n{e}</pre>"

# Ruta para ejecutar memoria.py
@app.route('/run-memoria')
def run_memoria():
    try:
        # Ejecutar el archivo de Python
        result = subprocess.run(['python3', 'memoria.py'], capture_output=True, text=True)
        # Devolver el resultado o error si ocurrió
        return f"<pre>{result.stdout}</pre>" if result.returncode == 0 else f"<pre>Error:\n{result.stderr}</pre>"
    except Exception as e:
        return f"<pre>Error ejecutando el archivo:\n{e}</pre>"

# Iniciar la aplicación Flask
if __name__ == '__main__':
    # Ejecutar en 0.0.0.0 y especificar el puerto
    app.run(host='0.0.0.0', port=5000, debug=True)

