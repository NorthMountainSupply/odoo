from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    ignore_in_manufacturable = fields.Boolean(
        string="Ignore in Manufacturable",
        help="If checked, this product will not be considered in the manufacturable computation. This should be checked for plastic bags or packing materials, where alternative items can be used.",
        related="product_tmpl_id.ignore_in_manufacturable",
    )

    manufacturable = fields.Float(
        string="Manufacturable",
        compute="_compute_manufacturable",
        help="The maximum amount of this product that can be made given the current inventory.",
        store=True,
        recursive=True,
    )

    # flag to prevent infinite recursion
    _computing_manufacturable = fields.Boolean(
        string="Computing Manufacturable",
        default=False,
        store=False,
    )

    @api.depends(
        "ignore_in_manufacturable",
        "bom_ids",
        "bom_ids.manufacturable",
        "qty_available",
    )
    def _compute_manufacturable(self) -> None:
        for product in self:
            if product._computing_manufacturable:
                continue
            product._computing_manufacturable = True
            try:
                if product.ignore_in_manufacturable:
                    product.manufacturable = 9999
                else:
                    max_bom_qty = max(product.bom_ids.mapped("manufacturable"), default=0)
                    product.manufacturable = product.qty_available + max_bom_qty
            finally:
                product._computing_manufacturable = False


class ProductTemplate(models.Model):
    _inherit = "product.template"

    ignore_in_manufacturable = fields.Boolean(
        string="Ignore in Manufacturable",
        help="If checked, this product will not be considered in the manufacturable computation. This should be checked for plastic bags or packing materials, where alternative items can be used.",
        store=True,
        copied=True,
    )

    manufacturable = fields.Float(
        string="Manufacturable",
        compute="_compute_manufacturable",
        help="The maximum amount of this product that can be made given the current inventory.",
        store=True,
    )

    @api.depends("product_variant_ids.manufacturable")
    def _compute_manufacturable(self) -> None:
        for template in self:
            template.manufacturable = max(template.product_variant_ids.mapped("manufacturable"), default=0)
