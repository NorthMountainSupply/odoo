from odoo import api, fields, models


class MrpBom(models.Model):
    _inherit = "mrp.bom"

    manufacturable = fields.Float(
        string="Manufacturable",
        compute="_compute_manufacturable",
        help="The maximum amount of this BoM that can be made given the current inventory.",
        store=True,
    )

    _computing_manufacturable = fields.Boolean(
        string="Computing Manufacturable",
        default=False,
        store=False,
    )

    @api.depends(
        "bom_line_ids",
        "bom_line_ids.product_qty",
        "bom_line_ids.product_id.manufacturable",
        "bom_line_ids.product_id.ignore_in_manufacturable",
    )
    def _compute_manufacturable(self) -> None:
        for bom in self:
            if bom._computing_manufacturable:
                continue
            bom._computing_manufacturable = True
            try:
                max_for_this_bom: float = float("inf")
                for line in bom.bom_line_ids:
                    component = line.product_id
                    if component.ignore_in_manufacturable:
                        continue
                    component_qty = component.manufacturable
                    if component_qty < line.product_qty:
                        max_for_this_bom = 0
                        break
                    max_for_this_bom = min(max_for_this_bom, component_qty / line.product_qty)
                if max_for_this_bom == float("inf"):
                    max_for_this_bom = 0
                bom.manufacturable = max_for_this_bom
            finally:
                bom._computing_manufacturable = False

    # prevent users from making circular BoM dependencies
    #
    # i tested this and Odoo already prevents circular dependencies so this was unnecessary lol
    #
    # @api.constrains("bom_line_ids")
    # def _check_circular_dependency(self):
    #    for bom in self:
    #        visited = set()
    #        self._check_circular_dependency_recursive(bom, visited)
    # def _check_circular_dependency_recursive(self, bom, visited):
    #    if bom in visited:
    #        raise ValidationError("Circular dependency detected in BoM.")
    #    visited.add(bom)
    #    for line in bom.bom_line_ids:
    #        if line.product_id.bom_ids:
    #            for child_bom in line.product_id.bom_ids:
    #                self._check_circular_dependency_recursive(child_bom, visited)
