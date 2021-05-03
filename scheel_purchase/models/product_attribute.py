# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProductTemplateAttributeValue(models.Model):
    _inherit = 'product.template.attribute.value'

    cost_extra = fields.Float(
        string="Value Cost Extra",
        default=0.0,
        digits='Product Price',
        help="Extra cost for the variant with this attribute value.")
