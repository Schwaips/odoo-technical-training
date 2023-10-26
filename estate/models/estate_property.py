from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False) #copy=False, default=fields.Date.today
    expected_price = fields.Float(required=True) # required=True
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
      string="Garden Orientation",
      selection=[("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")],
      help="Garden Orientation (North, South, East or West)"
    )