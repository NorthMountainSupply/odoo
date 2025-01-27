from odoo import fields, models


class BulkPO(models.Model):
    _name = "bulk.po"
    _description = "Bulk Purchase Order"

    # 6 Fields Automatically Added to the bulk.po Model by Odoo (all readonly):
    # create_date (datetime)
    # create_uid (many2one)
    # display_name (char)
    # id (integer)
    # write_date (datetime)
    # write_uid (many2one)

    name = fields.Char(string="Label", required=True)
    active = fields.Boolean(default=True)
