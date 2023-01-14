from odoo import models, fields, api, _

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrderInherit, self).action_confirm()
        print("insert_info_social_proof triggerd")
        for so in self:
            print("SO name = {} at state {}".format(so.name, so.state))
            partner_id = so.partner_id
            date_order = so.date_order
            if so.state == 'sale':
                for line in so.order_line:
                    if line.product_id.filtered(lambda productlist : productlist.type == 'product'):
                        scpf = self.env['social.proof'].create({
                            "product_id_c" : line.product_id.id,
                            "partner_id_c" : partner_id.id,
                            "address_c" : partner_id.state_id.id,
                            "time_c" : date_order,
                            "image_c" : line.product_id.image_1920,
                        })
                        print("social proof record created {}".format(scpf))
        

class SocialProof(models.Model):
    _name = 'social.proof'
    _description = 'Social Proof'

    product_id_c = fields.Many2one("product.product", string="Product Variant")
    product_tmpl_id_c = fields.Many2one(related='product_id_c.product_tmpl_id', string="Product Template")
    partner_id_c = fields.Many2one("res.partner", string="Customer")
    address_c = fields.Many2one("res.country.state", string="Address")
    time_c = fields.Char(string="Date")
    image_c = fields.Binary(string="Image")