from flask import Flask
import subprocess

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Ruta para ejecutar snake_test.py
@app.route('/run-python-code')
def run_python_code():
    # Ejecutar el archivo de Python
    result = subprocess.run(['python', 'snake_test.py'], capture_output=True, text=True)
    # Devolver el resultado
    return f"<pre>{result.stdout}</pre>"

# Ruta para ejecutar game.py
@app.route('/run-python-code2')
def run_python_code2():
    # Ejecutar el archivo de Python
    result = subprocess.run(['python', 'game.py'], capture_output=True, text=True)
    # Devolver el resultado
    return f"<pre>{result.stdout}</pre>"

# Ruta para ejecutar game.py
@app.route('/run-python-code3')
def run_python_code3():
    # Ejecutar el archivo de Python
    result = subprocess.run(['python', 'memoria.py'], capture_output=True, text=True)
    # Devolver el resultado
    return f"<pre>{result.stdout}</pre>"

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)


