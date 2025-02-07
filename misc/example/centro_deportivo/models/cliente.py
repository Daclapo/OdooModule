from itertools import tee
from odoo import models, fields, api


class cliente(models.Model):
    _name = 'centro_deportivo.cliente'
    _description = 'Clase destinada a los clientes del centro deportivo'
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required = True)
    apellidos = fields.Char('Apellidos', required = True)
    fecha_nacimiento = fields.Date('fecha de nacimiento',default = fields.date.today())
    sexo = fields.Selection([('h','Hombre'),('m','Mujer'),('o','Otro')])
    direccion = fields.Char('Direccion del domicilio')
    email = fields.Char('Correo electrónico')
    telf = fields.Integer(string='Número de teléfono',  size=9)
    imagen = fields.Binary('Foto de perfil', help='Introduzca la fotografía')
    servicios_ids = fields.Many2many('centro_deportivo.servicio', string='Servicios a los que está inscrito el cliente')
    pagado = fields.Boolean(string='¿Ha pagado la cuota?', default=False)
    total = fields.Float(string='Total actividades', compute='calculated_total')

    def calculated_total(self):
        for record in self:
            for precio_servicio in record.servicios_ids:
                record.total = record.total + precio_servicio.precio