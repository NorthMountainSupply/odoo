from odoo import fields, models


# Add Char field to template model for ASIN
class ProductTemplate(models.Model):
    _inherit = "product.template"

    asin = fields.Char(
        string="ASIN",
        help="The ASIN associated with this product listing.",
        store=True,
        indexed=True,
    )


# Add to the product model, just reads its parent's value
class ProductProduct(models.Model):
    _inherit = "product.product"

    asin = fields.Char(
        string="ASIN",
        help="The ASIN associated with this product listing.",
        related="product_tmpl_id.asin",
    )
