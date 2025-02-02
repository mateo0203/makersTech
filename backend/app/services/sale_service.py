from datetime import datetime
from app.DB import hardcoded_database


# Get all sales data
def get_sales_data():
    """Fetch all sales data from the hardcoded database."""
    results = []
    
    for sale in hardcoded_database.hardcoded_db["sales"]:
        # Find product details
        product = next((p for p in hardcoded_database.hardcoded_db["products"] if p["product_id"] == sale["product_id"]), None)

        # Structure the response
        results.append({
            "product_name": product["description"] if product else "Unknown Product",
            "brand": product["brand"] if product else "Unknown Brand",
            "product_type": product["product_type"] if product else "Unknown Type",
            "quantity_sold": sale["quantity"],
            "timestamp": sale["timestamp"]
        })
    
    return results
