# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class parking(models.Model):
#     _name = 'parking.parking'
#     _description = 'parking.parking'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

class garaje(models.Model):
    _name = 'parking.garaje'
    _description = 'Características de los garajes'

    name = fields.Char('Dirección', required=True)
    plazas = fields.Integer(string='Plazas', required=True)

    # relaciones entre tablas 
    coche_ids = fields.One2many('parking.coche', 'garaje_id', string='Coches')

class coche(models.Model):
    _name = 'parking.coche'
    _description = 'Características de los coches con plaza'
    _order = 'name'

    name = fields.Char(string='Matrícula', required=True, size=7)
    modelo = fields.Char(string='Modelo', required=True)
    construido = fields.Date(string='Fecha de fabricación')
    consumo = fields.Float('Consumo', (4, 1), default=0.0, help='Consumo promedio cada 100 kms')
    averiado = fields.Boolean(string='Averiado', default=False)
    #store=True no conveniente en este caso para recualcular al cambiar el año
    annos = fields.Integer('Años', compute='_get_annos')
    descripcion = fields.Text('Descripción')

    # relaciones entre tablas
    garaje_id = fields.Many2one ('parking.garaje', string='Garaje')
    mantenimiento_ids = fields.Many2many('parking.mantenimiento', string='Mantenimientos')

    @api.depends('construido')
    def _get_annos(self):
        
        for coche in self:
            hoy = date.today()
            coche.annos = relativedelta(hoy, coche.construido).years

    # restricciones, mismo formato que en la BD
    _sql_constraints=[('name_uniq', 'unique(name)', 'La matricula ya existe')]

class mantenimiento(models.Model):
    _name = 'parking.mantenimiento'
    _description = 'Mantenimientos a realizar en coches'
    _order = 'fecha'

    #name =fields.Char()
    fecha = fields.Date('Fecha', required=True, default = fields.date.today())
    tipo = fields.Selection(string='Tipo', selection=[('l','Lavado'),('r','Revisión'),('m','Mecánica'),('p','Pintura')], default='l')
    coste = fields.Float('Coste', (8,2), help='Coste total del mantenimiento')

    # relaciones entre tablas
    coche_ids = fields.Many2many('parking.coche', string='Coches')

    def name_get(self):
        resultados=[]
        for mantenimiento in self:
            descripcion = f'{len(mantenimiento.coche_ids)} coches - {mantenimiento.coste} €'
            resultados.append((mantenimiento.id, descripcion))
        return resultados