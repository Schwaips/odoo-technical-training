from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"

    name = fields.Char(required=True)
    # color = fields.Integer()
    property_ids = fields.Many2many("estate.property", string="Properties")