from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    topic = data.get('topic', 'general')
    platform = data.get('platform', 'Twitter')

    # Simulación de generación de contenido
    if platform == 'Twitter':
        content = f"Nuevo tweet sobre {topic}: ¡Descubre las últimas tendencias! #{{topic.replace(' ', '')}} #MarketingDigital"
    elif platform == 'LinkedIn':
        content = f"Artículo sobre {topic}: Cómo impacta en tu negocio. Lee más en nuestro blog. #{{topic.replace(' ', '')}} #Negocios #Innovación"
    elif platform == 'Instagram':
        content = f"¡Nueva imagen sobre {topic}! Dale like si te gusta. #{{topic.replace(' ', '')}} #Creatividad"
    else:
        content = f"Contenido generado para {platform} sobre {topic}."

    return jsonify({'content': content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
