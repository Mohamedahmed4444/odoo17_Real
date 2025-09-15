from odoo import models, fields, api

class PropertyHistory(models.Model):
    _name = 'property.history'
    _description = "Property History"

    user_id = fields.Many2one('res.users', string="User")
    property_id = fields.Many2one('property', string="Property")
    old_state = fields.Char(string="Old State")
    new_state = fields.Char(string="New State")
    change_date = fields.Datetime(string="Change Date", default=fields.Datetime.now)
    reason = fields.Char()