# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def _get_product_purchase_description(self, product_lang):
        description = super(PurchaseOrderLine, self)._get_product_purchase_description(product_lang)
        if len(product_lang.product_template_attribute_value_ids):
            for attribute in product_lang.product_template_attribute_value_ids:
                description += f'\n- {attribute.display_name} : {attribute.cost_extra}'
        return description

    def _prepare_compute_all_values(self):
        vals = super(PurchaseOrderLine, self)._prepare_compute_all_values()
        if len(self.product_id.product_template_attribute_value_ids):
            vals['price_unit'] += sum(self.product_id.mapped('product_template_attribute_value_ids.cost_extra'))
        return vals
