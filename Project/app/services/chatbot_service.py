#from openai import OpenAI

import google.generativeai as genai
import os
from app.config import Config
import inspect
import app.services.product_service as product_service
import app.services.sale_service as sale_service

# Load OpenAI API Key from config.py
aConfig = Config()
print(aConfig.GEMINI_API_KEY)
genai.configure(api_key=aConfig.GEMINI_API_KEY)
MODEL = "gemini-1.5-flash"  # You can change this to "gemini-1.5-flash" for faster responses

# 🔹 Dynamically Collect CRUD Functions
CRUD_SERVICES = {
    "get_all_products_inventory_data": product_service.get_all_products,
    "get_sales_data": sale_service.get_sales_data,
    "not_related_to_ecommerce_data": product_service.not_related_to_ecommerce_data
}

# 🔹 Generate Descriptions for OpenAI Prompt
CRUD_DESCRIPTIONS = {
    "get_all_products_inventory_data": "Obtener una lista de todos los productos junto con sus detalles de inventario, como disponibilidad, precio y cantidad.",
    "get_sales_data": "Obtener datos de ventas de todos los productos, incluyendo la cantidad vendida y la fecha de venta.",
    "not_related_to_ecommerce_data": "Este endpoint no está relacionado con datos de makers tech y maneja información independiente."
}

def determine_crud_operation(user_message: str):
    """Uses OpenAI to determine the appropriate CRUD function to call."""

    # Generate the AI prompt dynamically
    function_descriptions = "\n".join(
        [f"- {key}: {desc}" for key, desc in CRUD_DESCRIPTIONS.items()]
    )

    prompt = f"""
    Eres un asistente de inteligencia artificial para una tienda de comercio electrónico de tecnología. 
    Analiza el mensaje del usuario y determina qué acción se debe realizar.

    Acciones disponibles:
    {function_descriptions}

    Mensaje del usuario: "{user_message}"
    ¿Qué acción se debe realizar? Responde ÚNICAMENTE con uno de los siguientes nombres de función: 
    {", ".join(CRUD_SERVICES.keys())}.
    """

    # Generate response using Gemini API
    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(prompt)

    
    operation = response.candidates[0].content.parts[0].text.strip()

    return operation if operation in CRUD_SERVICES else None

# 🔹 Function to Extract Parameters from User Message
def extract_parameters(service_function, user_message):
    """Dynamically extracts parameters needed for the selected service function."""
    params = {}
    function_signature = inspect.signature(service_function)
    # 🔹 Get dynamic keyword mapping from the database
   #keyword_mapping = get_keyword_mapping(db)
       # 🔹 Hardcoded keyword mapping
    keyword_mapping = {
        "brand": ["Apple", "Samsung", "Dell", "HP"],
        "product_type": ["Laptop", "Smartphone", "Tablet", "Monitor"],
        "product_id": {
            "laptop apple": 1,
            "laptop dell": 2,
            "smartphone samsung": 3,
            "tablet apple": 4,
            "monitor hp": 5
        }
    }

    # 🔹 Ensure we only assign the correct keywords to their matching parameter
    for param in function_signature.parameters:
        if param == "brand":  # ✅ Only assign brands to brand
            for brand in keyword_mapping["brand"]:
                if brand.lower() in user_message.lower():
                    params["brand"] = brand
                    break  # Stop once a match is found

        elif param == "product_type":  # ✅ Only assign product types to product_type
            for product_type in keyword_mapping["product_type"]:
                if product_type.lower() in user_message.lower():
                    params["product_type"] = product_type
                    break  # Stop once a match is found

    # 🔹 Handle product_id separately
    for product_name, product_id in keyword_mapping["product_id"].items():
        if product_name in user_message.lower():
            params["product_id"] = product_id

    return params

# 🔹 Generate AI-Powered Response Based on Query Result
def generate_ai_response(user_message: str, query_result):
    """Uses OpenAI to generate a natural language response based on query results."""

    prompt = f"""
        Eres un asistente de IA para una tienda de comercio electrónico de tecnología.  
        Tu tarea es convertir los resultados de consultas estructuradas en respuestas en lenguaje natural.  

        Pregunta del usuario: "{user_message}"  

        Resultado de la consulta:  
        {query_result}  

        Responde de manera natural y amigable para el usuario.  
    """
    print(f"Este es el query que le estamos dando a la IA: {prompt}")


    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(prompt)
    response.candidates[0].content.parts[0].text.strip()
    return response.candidates[0].content.parts[0].text.strip()




def chatbot_response(user_message: str):
    """Determines the CRUD action, extracts parameters dynamically, executes the service function, and formats the response with AI."""
    operation = determine_crud_operation(user_message)
    print(f"Operation: {operation}")
    if not operation:
        return {"error": "Could not determine the appropriate action."}
    
    print("Passes the error...")
    
    # 🔹 Get the function from the services layer
    service_function = CRUD_SERVICES[operation]
    
    # 🔹 Extract parameters dynamically using database values
    params = extract_parameters(service_function, user_message)

    # 🔹 Call the service function with extracted parameters
    print(f"The parameter: {params}")
    result = service_function(**params)

    # 🔹 Generate AI-powered response
    ai_response = generate_ai_response(user_message, result)

    return {"response": ai_response}
