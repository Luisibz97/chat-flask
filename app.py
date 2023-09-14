from flask import Flask, render_template, request
from analizador_sentimientos import AnalizadorDeSentimientos, openai, messages

analizador = AnalizadorDeSentimientos()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_prompt = request.form['user_input']
    # Lógica para interactuar con el chatbot y obtener la respuesta y el sentimiento
    # Puedes usar subprocess, llamadas a sistemas, etc. para ejecutar 'analizador_sentimientos.py'
    # y obtener la respuesta del chatbot aquí
    # Supongamos que la respuesta del chatbot se almacena en la variable 'respuesta' y el sentimiento en 'sentimiento'
    return render_template('chat.html', user_input=user_prompt, respuesta=respuesta, sentimiento=sentimiento)

if __name__ == '__main__':
    app.run(debug=True)
