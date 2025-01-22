from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    can_be_manufactured = fields.Float(string="Can Be Manufactured", compute="_compute_can_be_manufactured")

    # Compute method for the Can Be Manufactured field
    @api.depends("bom_ids", "bom_ids.bom_line_ids", "bom_ids.bom_line_ids.product_id.can_be_manufactured", "qty_available")
    def _compute_can_be_manufactured(self):
        def compute_recursive(product, visited):
            # Only compute components once, prevents infinite loops
            if product.id in visited:
                return product.can_be_manufactured
            visited.add(product.id)

            max_qty = 0
            for bom in product.bom_ids:
                max_for_this_bom = float("inf")
                for line in bom.bom_line_ids:
                    component = line.product_id
                    component_qty = compute_recursive(component, visited)
                    if component_qty < line.product_qty:
                        max_for_this_bom = 0
                        break
                    max_for_this_bom = min(max_for_this_bom, component_qty / line.product_qty)
                if max_for_this_bom == float("inf"):
                    max_for_this_bom = 0
                max_qty = max(max_qty, max_for_this_bom)
            return max_qty + product.qty_available

        for product in self:
            visited = set()
            product.can_be_manufactured = compute_recursive(product, visited)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    can_be_manufactured = fields.Float(string="Can Be Manufactured", compute="_compute_can_be_manufactured")

    @api.depends("product_variant_ids.can_be_manufactured")
    def _compute_can_be_manufactured(self):
        for template in self:
            template.can_be_manufactured = min(template.product_variant_ids.mapped("can_be_manufactured"), default=0)
