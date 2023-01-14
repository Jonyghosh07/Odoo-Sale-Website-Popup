import json
from odoo import models, fields, api, _
from odoo import http

class ProductLoop(http.Controller):
    @http.route('/get/proofs', auth='public', type='http', methods=['GET'], website=True)
    def index(self, **kw):
        proofs = http.request.env['social.proof'].sudo().search([], limit=10, order='create_date DESC')
        product_list=[]
        for proof in proofs:
            product_list.append({
                "cus_name": proof.partner_id_c.name,
                "cus_loc": proof.partner_id_c.state_id.name,
                "prod_id" : proof.product_tmpl_id_c.id,
                "prod_name": proof.product_tmpl_id_c.name,
                "prod_img":proof.image_c.decode("utf-8") if proof.image_c else None,
                "sale_datetime": proof.time_c,  
            })
        return json.dumps(product_list)