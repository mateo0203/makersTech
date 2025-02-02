# Makers Tech ChatBot

## Descripción

**Makers Tech ChatBot** es una aplicación interactiva que permite a los usuarios consultar el inventario y obtener información sobre productos de tecnología en tiempo real utilizando un chatbot basado en IA. A través de un sistema de preguntas y respuestas en lenguaje natural, los usuarios pueden obtener información sobre la disponibilidad de productos, características y precios de manera eficiente, sin tener que navegar por varias páginas del sitio.

La aplicación se basa en un modelo de lenguaje (GPT de OpenAI) y se conecta a una base de datos SQLite para realizar consultas SQL en tiempo real, proporcionando respuestas personalizadas.

## Tecnologías Usadas

- **Frontend**: 
  - **JavaScript**
  - **React.js**
  - **MUI (Material-UI)** para diseño y componentes de interfaz
- **Backend**:
  - **Python**
  - **Flask** para el servicio web
  - **Flask-CORS** para habilitar la comunicación entre el frontend y el backend
  - **SQLite** para la base de datos de inventario
- **IA**:
  - **Langchain** para integrar el modelo de lenguaje GPT con la base de datos
  - **OpenAI API** para el modelo de lenguaje (GPT-3.5)

## Uso

La aplicación está diseñada para permitir a los usuarios interactuar con el chatbot a través de una interfaz gráfica. Puedes escribir preguntas en lenguaje natural y el chatbot se encargará de generar consultas SQL y devolver las respuestas de la base de datos en formato legible.
Ejemplos de preguntas que puedes hacer:
"¿Cuántos productos HP hay disponibles?"
"¿Cuáles son las características del producto 'Laptop Dell'?"
"¿Cuánto cuesta el 'Teclado mecánico'?"
El chatbot responderá con la información relevante según la base de datos.


