from odoo import models, fields, api


class SaleOrder(models.Model):

    _inherit = "sale.order"
    ship_id = fields.Many2one('ship.property', string="Ship")

    @api.onchange
    def onchange_ship_id(self,ship_id):
        return

    def get_update(self):
        if self.ship_id:
            for line in self.order_line:
                line.write({'ship_id': self.ship_id})


class ShipProperty(models.Model):
    _name = 'ship.property'
    _rec_name = 'imo'
    _description = "ship_property"
    imo = fields.Char(string="IMO",required=True)
    hull_number = fields.Char()
    engine_number = fields.Char()
    vessel_name = fields.Char()
    build_year = fields.Char()
    _sql_constraints = [('imo', 'unique(imo)', 'imo must be unique!')]
    partner_id = fields.Many2one('res.partner', string='Shipyard')
    owner_id = fields.Many2one('res.partner', string='ShipOwner')
    ShipManagement_id = fields.Many2one('res.partner', string='ShipManagement')
    EngineBuilder_id = fields.Many2one('res.partner', string='EngineBuilder')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # @api.onchange('ship_id')
    # def onchange_product_id(self):
    #     self.ship_id = self.product_id.ship_id
    # #
    # @api.model
    # def _default_ship(self):
    #     return self.ship_id
    ship_id = fields.Many2one('ship.property', string="Ship",default=lambda
        self: self.env['ship.property'].search([('imo','=','DRYT')]))


