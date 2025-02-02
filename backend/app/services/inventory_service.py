from app.DB import hardcoded_database

# 🔹 Get inventory details by brand and product type
def get_inventory_by_brand_and_product_type(brand: str = None, product_type: str = None):
    """Fetch inventory details filtered by brand and product type from the hardcoded database."""
    results = []
    for inventory_item in hardcoded_database.hardcoded_db["inventory"]:
        product = next((p for p in hardcoded_database.hardcoded_db["products"] if p["product_id"] == inventory_item["product_id"]), None)
        
        if not product:
            continue  # Skip if product not found

        # Apply filters
        if brand and product["brand"].lower() != brand.lower():
            continue
        if product_type and product["product_type"].lower() != product_type.lower():
            continue

        # Add to result
        results.append({
            "product_id": inventory_item["product_id"],
            "brand": product["brand"],
            "product_type": product["product_type"],
            "available": inventory_item["available"],
            "price": inventory_item["price"],
            "quantity": inventory_item["quantity"]
        })
    
    return results

def get_inventory_by_brand(brand: str):
    """Fetch inventory details filtered by brand from the hardcoded database."""
    results = []
    for inventory_item in hardcoded_database.hardcoded_db["inventory"]:
        product = next((p for p in hardcoded_database.hardcoded_db["products"] if p["product_id"] == inventory_item["product_id"]), None)
        
        if not product:
            continue  # Skip if product not found

        # Apply brand filter
        if product["brand"].lower() != brand.lower():
            continue

        # Add to result
        results.append({
            "product_id": inventory_item["product_id"],
            "brand": product["brand"],
            "product_type": product["product_type"],
            "available": inventory_item["available"],
            "price": inventory_item["price"],
            "quantity": inventory_item["quantity"]
        })
    return results

# 🔹 Get inventory details by product type
def get_inventory_by_product_type(product_type: str = None):
    """Fetch inventory details filtered by product type from the hardcoded database."""
    results = []
    for inventory_item in hardcoded_database.hardcoded_db["inventory"]:
        product = next((p for p in hardcoded_database.hardcoded_db["products"] if p["product_id"] == inventory_item["product_id"]), None)
        
        if not product:
            continue  # Skip if product not found

        # Apply product type filter
        if product_type and product["product_type"].lower() != product_type.lower():
            continue

        # Add to result
        results.append({
            "product_id": inventory_item["product_id"],
            "brand": product["brand"],
            "product_type": product["product_type"],
            "available": inventory_item["available"],
            "price": inventory_item["price"],
            "quantity": inventory_item["quantity"]
        })
    return results

# 🔹 Get all inventory details (no filters)
def get_all_inventory():
    """Fetch all inventory details from the hardcoded database."""
    results = []
    for inventory_item in hardcoded_database.hardcoded_db["inventory"]:
        product = next((p for p in hardcoded_database.hardcoded_db["products"] if p["product_id"] == inventory_item["product_id"]), None)
        
        if not product:
            continue  # Skip if product not found

        # Add to result (No filters)
        results.append({
            "product_id": inventory_item["product_id"],
            "brand": product["brand"],
            "product_type": product["product_type"],
            "available": inventory_item["available"],
            "price": inventory_item["price"],
            "quantity": inventory_item["quantity"]
        })
    return results

# 🔹 Get total stock count
def get_total_stock():
    """Returns the total count of available products in inventory."""
    total_stock = sum(item["quantity"] for item in hardcoded_database.hardcoded_db["inventory"] if item["available"])
    return {"total_items": total_stock}
