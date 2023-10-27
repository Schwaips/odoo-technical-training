from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime

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
    # a property can have ONE type but a type can have MANY properties
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)
    partner_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    # a property can have MANY tags and a tag can have MANY properties
    tag_ids = fields.Many2many("estate.property.tag", string="Property Tags")

    # a property can have MANY offers and an offer can have ONE property
    # dans les paramètres de la relation, on spécifie en premier lieu, le model avec lequel on veut créer la relation
    # puis on spécifie en second lieu, on précise quel champ on va utiliser sur le model spécifié en premier parametre. (ici : le champ property_id du model estate.property.offer)
    # "estate.property.offer" est donc le model avec lequel on veut créer la relation
    # et property_id fait référence à l'instance du model estate.property (model sur lequel se trouve)
    # Si il y a une relation One2Many sur estate.property.offer, alors il y a une relation Many2One sur estate.property.offer 
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")