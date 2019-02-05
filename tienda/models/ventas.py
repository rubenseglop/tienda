from odoo import models, fields, api


class Ventas(models.Model):
    _name = 'tienda.ventas'

    cliente = fields.Many2one('tienda.clientes', 'Cliente')
    fecha_actual = fields.Date(string='Fecha actual', default=lambda s: fields.Date.context_today(s))
    articulo = fields.Many2one('tienda.articulos', 'Artículo')
    cantidad = fields.Integer('Cantidad', required=True)
    precio = fields.Float('PVP/u')
    total = fields.Float(string='Precio total', compute='_total')

    @api.one
    @api.depends('precio','cantidad')
    def _total(self):
        #self.total= self.precio * self.cantidad
        cursor = self.env.cr
        ##cursor.execute('select * from tienda_articulos where cod=%s' (self.articulo.cod,))
        cursor.execute('select precio from tienda_articulos where cod=%s' , (self.articulo.cod,))
        for x in cursor.fetchall():
            self.precio=x[0]
            self.total = self.total + (self.precio * self.cantidad)
