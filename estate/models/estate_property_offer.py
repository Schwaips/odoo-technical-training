from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta

class EstatePropertyOffer(models.Model):
  _name = "estate.property.offer"
  _description = "Real Estate Property Offer"
  _order = "price desc"

  price = fields.Float()
  status = fields.Selection(
    string="Status",
    selection=[("accepted", "Accepted"), ("refused", "Refused")],
    copy=False,
  )
  partner_id = fields.Many2one("res.partner", string="Buyer", required=True)
  property_id = fields.Many2one("estate.property", string="Property", required=True)
  date_deadline = fields.Date(string="Deadline", required=True, compute="_compute_date_deadline", inverse="_inverse_date_deadline")
  validity = fields.Integer(string="Validity (in days)", required=True, default=7)

  _sql_constraints = [
      ('check_price', 'CHECK(price > 0)', 'Price must be positive!'),
  ]

  @api.depends("validity")
  def _compute_date_deadline(self):
    for record in self:
      if not record.exists():
        continue
      record.date_deadline = record.create_date or fields.Date.today() + timedelta(days=record.validity)

  def _inverse_date_deadline(self):
    for record in self:
      record.validity = (record.date_deadline - fields.Date.today()).days

  def _has_offer_id_accepted(self, offers):
    return any(offer.status == "accepted" for offer in offers)

  def action_confirm_offer(self):
    for offer in self:
      estate_property = offer.property_id

      if self._has_offer_id_accepted(estate_property.offer_ids):
        raise UserError("An offer has been already accepted for this property.")
      else:
        offer.status = "accepted"
        offer.property_id.selling_price = offer.price
        offer.property_id.state = "offer_accepted"
        offer.property_id.partner_id = offer.partner_id.id

  def action_refuse_offer(self):
    for offer in self:
      offer.status = "refused"