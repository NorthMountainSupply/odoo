from typing import Set

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

    # Compute method for the Manufacturable field
    @api.depends(
        "ignore_in_manufacturable",
        "bom_ids",
        "bom_ids.bom_line_ids",
        "bom_ids.bom_line_ids.product_qty",
        "bom_ids.bom_line_ids.product_id.manufacturable",
        "qty_available",
    )
    def _compute_manufacturable(self) -> None:
        def compute_recursive(product: ProductProduct, visited: Set[int]) -> float:
            # Only compute components once, prevents infinite loops
            if product.id in visited:
                return product.manufacturable
            visited.add(product.id)

            if product.ignore_in_manufacturable:
                return 9999

            max_qty: float = 0.0
            for bom in product.bom_ids:
                max_for_this_bom: float = float("inf")
                for line in bom.bom_line_ids:
                    component: ProductProduct = line.product_id
                    component_qty: float = compute_recursive(component, visited)
                    if component_qty < line.product_qty:
                        max_for_this_bom = 0
                        break
                    max_for_this_bom = min(max_for_this_bom, component_qty / line.product_qty)
                if max_for_this_bom == float("inf"):
                    max_for_this_bom = 0
                max_qty = max(max_qty, max_for_this_bom)
            return max_qty + product.qty_available

        for product in self:
            visited: Set[int] = set()
            product.manufacturable = compute_recursive(product, visited)


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
            template.manufacturable = min(template.product_variant_ids.mapped("manufacturable"), default=0)
