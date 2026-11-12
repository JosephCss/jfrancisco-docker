from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi Primer Docker con Flask</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; text-align: center; padding: 50px; }
            .card { background: white; border-radius: 12px; padding: 40px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); display: inline-block; }
            h1 { color: #0db7ed; }
            p { color: #333; font-size: 1.1em; }
            .badge { background: #28a745; color: white; padding: 6px 14px; border-radius: 20px; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>!HOLA JOSEPH ALMACHI! 🐳</h1>
            <p>Mi primera aplicación web contenerizada.</p>
            <span class="badge">Ejecutándose en un contenedor Linux con WSL 2</span>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    # Importante: host="0.0.0.0" permite conexiones externas al contenedor
    app.run(host="0.0.0.0", port=5000)
