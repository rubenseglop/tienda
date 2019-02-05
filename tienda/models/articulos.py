from odoo import models, fields, api


class Articulos(models.Model):
    _name = 'tienda.articulos'

    cod = fields.Integer('COD', required=True)
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripción', required=True)
    #proveedor = fields.Char('Proveedor', required=True)
    proveedor = fields.Many2one('tienda.proveedores', 'Proveedor')
    precio = fields.Float('Precio', required=True)
    cantidad = fields.Integer('Cantidad', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

