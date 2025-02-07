from odoo import models, fields, api


class servicio(models.Model):
    _name = 'centro_deportivo.trabajador'
    _description = 'Clase destinada a los trabajadores del centro deportivo'
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    sexo = fields.Selection([('h','Hombre'),('m','Mujer'),('o','Otro')])
    nss = fields.Char('Numero de la Seguridad Social')
    fecha_nacimiento = fields.Date('Fecha de nacimiento', default = fields.date.today())
    telf = fields.Integer('Numero de telefono', size=9)
    imagen = fields.Binary('Imagen', help='Introduzca la fotografía')

    servicios_ids = fields.Many2many('centro_deportivo.servicio', string='Servicios que imparte como monitor este trabajador')
