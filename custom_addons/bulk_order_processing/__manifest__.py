{
    "name": "Bulk Order Processing",
    "version": "1.0",
    "category": "Sales",
    "summary": "App for managing Bulk POs.",
    "author": "Colby Heaton",
    "depends": ["product", "mrp", "sale_management", "asin_field", "manufacturable_field"],
    "data": [
        "security/ir.model.access.csv",
        "views/bulk_po.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "application": True,
}
