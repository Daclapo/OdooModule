from odoo import models, fields, api


class servicio(models.Model):
    _name = 'centro_deportivo.servicio'
    _description = 'Clase destinada a la gestión de servicios del centro deportivo'
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripcion')
    imagen = fields.Binary('Imagen', help='imagen del servicio')
    precio = fields.Float('Precio mensual', required=True)

    # relaciones entre tablas
    centros_ids = fields.Many2many('centro_deportivo.centro', string='Centros donde se imparte esta actividad')