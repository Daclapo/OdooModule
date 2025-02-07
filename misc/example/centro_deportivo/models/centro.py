from odoo import models, fields, api


class centro(models.Model):
    _name = 'centro_deportivo.centro'
    _description = 'Clase destinada a los centros deportivos'
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required = True)
    direccion = fields.Char('Calle del centro', required = True)
    localidad = fields.Char('Localidad')
    pais = fields.Char('Pais')
