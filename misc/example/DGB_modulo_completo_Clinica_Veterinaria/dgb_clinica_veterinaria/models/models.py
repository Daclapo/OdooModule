# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
class dgb_clinica_veterinaria(models.Model):
    _name = 'dgb_clinica_veterinaria.dgb_clinica_veterinaria'
    _description = 'dgb_clinica_veterinaria.dgb_clinica_veterinaria'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class mascota(models.Model):
    _name = 'dgb_clinica_veterinaria.mascota'
    _description = 'mascotas registradas en el centro'

    name = fields.Char('Nombre', required=True)
    ids_numchip = fields.Char('Numero chip', required=True)
    edad = fields.Integer('Edad', compute='_edad')
    #-----------------------
    @api.depends('nacimiento', 'edad')
    def _edad(self):
        self.edad = datetime.date.today().year - self.nacimiento.year
    #-----------------------
    nacimiento = fields.Date('Año en que nacio', required=True, default=fields.Date.context_today)
    peso = fields.Float('Peso')
    sexo = fields.Selection([('m','Macho'), ('h','Hembra'),],'Sexo' )
    raza = fields.Char('Raza', required=True)


    #Relaciones
    ndueno_id = fields.Many2one('dgb_clinica_veterinaria.duenio', 'Dueño')
    #Ahora con dueño referenciado cogemos los campos que queremos
    duenio_nombre = fields.Char(related='ndueno_id.name', string='Nombre del dueño')
    duenio_dni = fields.Char(related='ndueno_id.ids_dni', string='DNI del dueño')
    #
    vacuna_id = fields.Many2one('dgb_clinica_veterinaria.vacunas', string='Vacuna')
    vacuna_nombre = fields.Char(related='vacuna_id.name', string='Nombre de la vacuna')
    vacuna_num_lote = fields.Char(related='vacuna_id.ids_vacuna', string='Número de lote de la vacuna')
    fecha_vacuna = fields.Date('Fecha de vacunación')

class veterinario(models.Model):
    _name = 'dgb_clinica_veterinaria.veterinario'
    _description = 'Datos del veterinario/a'

    name = fields.Char('Nombre del Veterinario/a')
    telefono_vet = fields.Char('Telefono')
    turno = fields.Boolean(string='Turno de tarde', default=False)
    ids_numcolegiado = fields.Char()
#El nombre es demasiado largo con este codigo asignamos a la relacion u nombre mas corto
#no se acaba usando
    mascotas_atendidas = fields.Many2many('dgb_clinica_veterinaria.mascota', 
                                          'veterinario_mascota_rel',
                                          'veterinario_id',
                                          'mascota_id',
                                          string='Mascotas Atendidas')

class duenio(models.Model):
    _name = 'dgb_clinica_veterinaria.duenio'
    _description = 'Datos del tutor/cliente'

    name = fields.Char('Nombre del tutor')
    ids_dni = fields.Char('DNI del tutor')
    telefono = fields.Char('Telefono del tutor')
    email = fields.Text('e-mail')
    direccion = fields.Text('Direccion')

#El nombre es demasiado largo con este codigo asignamos a la relacion u nombre mas corto
    mascotas = fields.One2many('dgb_clinica_veterinaria.mascota', 'ndueno_id', string='Mascotas')
    
    mascota_names = fields.Char(string='Nombres de las mascotas', compute='_compute_mascota_info')

class vacunas(models.Model):
    _name = 'dgb_clinica_veterinaria.vacunas'
    _description = 'Vacunas disponibles en la clinica'

    name = fields.Char('Nombre de la vacuna')
    ids_vacuna = fields.Char('Numero de lote')
    precio = fields.Float()
    cantidad = fields.Integer()