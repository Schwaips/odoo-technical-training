from odoo import models, fields, api
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

  @api.depends("validity")
  def _compute_date_deadline(self):
    for record in self:
      if not record.exists():
        continue
      record.date_deadline = record.create_date or fields.Date.today() + timedelta(days=record.validity)

  def _inverse_date_deadline(self):
    for record in self:
      record.validity = (record.date_deadline - fields.Date.today()).days