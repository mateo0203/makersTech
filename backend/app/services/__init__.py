from app.services.product_service import (
    create_product,
    get_all_products,
    get_product_by_id,
    delete_product
)

from app.services.inventory_service import (
    get_inventory_by_brand,
    get_total_stock
)

from app.services.sale_service import (
    create_sale,
    get_sales_data
)

from app.services.chatbot_service import (
    chatbot_response,
    determine_crud_operation
)