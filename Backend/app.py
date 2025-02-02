from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.utilities import SQLDatabase
from langchain_community.chat_models import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
import os
from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
app = Flask(__name__)
# Habilita CORS para el endpoint /consulta
CORS(app, resources={r"/consulta": {"origins": "http://localhost:3000"}})

# Configuración de la base de datos y el modelo
db = SQLDatabase.from_uri("sqlite:///inventory.db")
llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo',
                 openai_api_key=OPENAI_API_KEY)
cadena = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=False)

formato = """
Dada una pregunta del usuario:
1. Crea una consulta SQL válida para PostgreSQL.
2. Ejecuta la consulta y revisa los resultados.
3. Devuelve el dato en formato legible.
4. Siempre responde en español.
#{question}
"""


@app.route('/consulta', methods=['POST'])
def consulta():
    try:
        data = request.json
        input_usuario = data.get('question')
        consulta = formato.format(question=input_usuario)
        resultado = cadena.run(consulta)
        return jsonify({"response": resultado})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
