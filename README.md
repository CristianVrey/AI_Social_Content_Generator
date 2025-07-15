![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)

# AI Social Content Generator

Una herramienta web para generar ideas y borradores de contenido para redes sociales, impulsada por IA (simulada inicialmente).

## Características (MVP)

- Interfaz web simple para ingresar tema y plataforma.
- Generación de borradores de posts para Twitter, LinkedIn, Instagram.

## Demo en Vivo

[Enlace a la demo en vivo aquí (ej. Heroku, Vercel, Netlify)]

## Screenshots / GIFs

![Captura de pantalla de la aplicación](enlace_a_tu_imagen_o_gif_aqui)

## Tecnologías

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript
- **Contenedores:** Docker
- **IA:** Ollama (con modelo Gemma 3)

## Cómo Ejecutar (Desarrollo)

Para ejecutar este proyecto, necesitarás tener **Docker** y **Ollama** instalados en tu sistema.

1.  **Instala Docker:** Sigue las instrucciones en [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
2.  **Instala Ollama:** Sigue las instrucciones en [https://ollama.com/download](https://ollama.com/download)
3.  **Descarga el modelo Gemma 3:** Una vez instalado Ollama, abre tu terminal y ejecuta:
    `ollama run gemma3`
    (Espera a que la descarga se complete y luego puedes escribir `bye` para salir del prompt interactivo).

4.  Clona este repositorio:
    `git clone https://github.com/CristianVrey/AI_Social_Content_Generator.git`
5.  Navega al directorio del proyecto:
    `cd AI_Social_Content_Generator`
6.  Construye y levanta los contenedores Docker:
    `docker-compose up --build`

La aplicación estará disponible en `http://localhost:8080`.

## Roadmap (Futuro)

- Integración con APIs de LLMs (OpenAI, Gemini) para generación de contenido real.
- Soporte para más plataformas de redes sociales.
- Funcionalidades de guardado y edición de borradores.
- Autenticación de usuarios.

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.