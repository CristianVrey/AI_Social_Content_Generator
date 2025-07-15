document.getElementById('generateBtn').addEventListener('click', async () => {
    const topic = document.getElementById('topic').value;
    const platform = document.getElementById('platform').value;
    const generatedContent = document.getElementById('generatedContent');

    if (!topic) {
        generatedContent.value = 'Por favor, ingresa un tema.';
        return;
    }

    try {
        const response = await fetch('http://localhost:5000/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ topic, platform })
        });

        const data = await response.json();
        generatedContent.value = data.content;
    } catch (error) {
        console.error('Error al generar contenido:', error);
        generatedContent.value = 'Error al conectar con el backend.';
    }
});
