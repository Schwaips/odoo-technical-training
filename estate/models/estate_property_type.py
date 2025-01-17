from odoo import models, fields

class EstatePropertyType(models.Model):
  _name = "estate.property.type"
  _description = "Real Estate Property Type"
  _order = "name"

  name = fields.Char(required=True)
  
  _sql_constraints = [
    ('name_unique', 'unique(name)', 'Type name already exists!'),
  ]

  property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
