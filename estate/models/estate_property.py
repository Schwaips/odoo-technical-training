from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda self: datetime.today() + relativedelta(months=+3))
    expected_price = fields.Float(required=True) # required=True
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
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
    active = fields.Boolean(default=True)
    state = fields.Selection(
      string="Status",
      selection=[("new", "New"), ("offer_received", "Offer Received"), ("offer_accepted", "Offer Accepted"), ("sold", "Sold"), ("canceled", "Canceled")],
      copy=False,
      required=True,
      default="new",
      help="Sales process stage"
    )