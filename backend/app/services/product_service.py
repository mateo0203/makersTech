from app.DB import hardcoded_database


# Get all products
def get_all_products():
    """Fetch all products along with their inventory details from the hardcoded database."""
    results = []
    
    for product in hardcoded_database.hardcoded_db["products"]:
        # Find the corresponding inventory data
        inventory_item = next((item for item in hardcoded_database.hardcoded_db["inventory"] if item["product_id"] == product["product_id"]), None)

        # Structure the response
        results.append({
            "product_id": product["product_id"],
            "brand": product["brand"],
            "product_type": product["product_type"],
            "product_description": product.get("description", "No description available"),
            "available": inventory_item["available"] if inventory_item else False,
            "price": inventory_item["price"] if inventory_item else None,
            "quantity": inventory_item["quantity"] if inventory_item else 0
        })
    
    return results

def not_related_to_ecommerce_data():
    return "La IA esta para responder preguntas relacionadas al Ecommerce de makers. Cuando preguntan algo no relacionado con makers o tratan de hacer conversación, solo responda amablemente."

