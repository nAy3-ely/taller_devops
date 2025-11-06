# nayhely.py (VERSION CON FLASK PARA DESPLIEGUE EN RENDER)

from flask import Flask
from datetime import datetime

# La aplicación Flask se inicializa aquí
app = Flask(__name__)

# Definimos el puerto que Render usará
PORT = 10000

@app.route("/")
def home():
    """Ruta principal que muestra el mensaje del taller."""
    
    # Crea el mensaje HTML
    html_content = f"""
    <html>
    <head><title>Taller Nayhely Valle - Flask</title></head>
    <body>
        <h1>👋 ¡Hola! Este es mi Taller de Contenedores con Flask</h1>
        <p>El framework web usado es: **Flask** (v2.2.5, según requirements.txt)</p>
        <p>La fecha y hora actual del contenedor es: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>✅ El servicio Docker está funcionando correctamente en Render.</p>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    # Flask sirve la aplicacion, escuchando en el puerto 10000
    print(f"Flask App iniciada en el puerto {PORT}")
    app.run(host='0.0.0.0', port=PORT)