from odoo import models, fields

class Tag(models.Model):
    _name = 'tag'
    _description = 'Tag'

    name = fields.Char(required=True)
    phone = fields.Char()
    address = fields.Char()
    property_ids = fields.Many2many('property', string="Properties")
