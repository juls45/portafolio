# Importaciones
from flask import Flask, render_template, request

# Instancia de la app
app = Flask(__name__)

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    # Inicializamos variables en None
    button_python = None
    button_discord = None
    button_html = None
    button_db = None

    # Si se recibe un POST (formulario enviado)
    if request.method == 'POST':
        button_python = request.form.get('button_python')
        button_discord = request.form.get('button_discord')
        button_html = request.form.get('button_html')
        button_db = request.form.get('button_db')

    # Renderizamos el HTML pasando las variables
    return render_template(
        'index.html',
        button_python=button_python,
        button_discord=button_discord,
        button_html=button_html,
        button_db=button_db
    )

# Ejecución
if __name__ == "__main__":
    app.run(debug=True)
