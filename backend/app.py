from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) # Habilita CORS para todas las rutas

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    topic = data.get('topic', 'general')
    platform = data.get('platform', 'Twitter')

    # Prompt refinado para Ollama
    prompt = f"Genera un post para {platform} sobre el tema: {topic}. El tono debe ser una mezcla de informal, divertido, directo, provocador, educativo y con un toque de venta, dirigido a un público general. Asegúrate de incluir hashtags relevantes y pegadizos al final del post."

    try:
        response = requests.post(
            "http://host.docker.internal:11434/api/generate", # Usamos host.docker.internal para acceder a Ollama en el host
            json={
                "model": "gemma3",
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status() # Lanza una excepción para códigos de estado de error (4xx o 5xx)
        ollama_response = response.json()
        generated_text = ollama_response["response"]

    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con Ollama: {e}")
        generated_text = f"Error: No se pudo conectar con el modelo de IA. Asegúrate de que Ollama esté corriendo y el modelo 'gemma3' esté descargado. ({e})"
    except KeyError:
        print(f"Respuesta inesperada de Ollama: {ollama_response}")
        generated_text = "Error: Respuesta inesperada del modelo de IA."

    return jsonify({'content': generated_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)