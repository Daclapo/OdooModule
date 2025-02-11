# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class dcp_library(models.Model):
#     _name = 'dcp_library.dcp_library'
#     _description = 'dcp_library.dcp_library'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')h
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100




# -*- coding: utf-8 -*-

from odoo import models, fields, api

class libro(models.Model):
    _name = 'dcp_library.libro'
    _description = 'Libro de la biblioteca'

    isbn = fields.Char(string="ISBN", required=True, help="Identificador único del libro")
    titulo = fields.Char(string="Título", required=True)
    autor_id = fields.Many2one('dcp_library.autor', string="Autor", required=True, ondelete="cascade")
    fecha_publicacion = fields.Date(string="Fecha de publicación", required=True)
    editorial = fields.Char(string="Editorial")
    edicion = fields.Char(string="Edición")
    numero_categoria = fields.Integer(string="Número de categoría", help="Número que indica la categoría según el Sistema Dewey")
    valor = fields.Float(string="Valor económico")
    en_biblioteca = fields.Boolean(string="En biblioteca", default=True)
    estado = fields.Selection(selection=[('nuevo', 'Nuevo'), ('usado', 'Usado'), ('deteriorado', 'Deteriorado')], string="Estado", required=True)


	# RELACIONES
    # Relación con el modelo 'prestamo'
    prestamos_ids = fields.One2many('dcp_library.prestamo', 'libro_prestado_id', string="Préstamos")

    # Relación Many2many con clientes que marcan el libro como favorito.
    # La tabla intermedia se llamará 'cliente_favoritos'
    cliente_ids = fields.Many2many('dcp_library.cliente', 'cliente_favoritos', 'libro_id', 'cliente_id', string="Clientes que marcaron este libro como favorito")

    _sql_constraints = [('isbn_unique', 'unique(isbn)', 'El ISBN debe ser único.')]



class autor(models.Model):
    _name = 'dcp_library.autor'
    _description = 'Autor de libros'

    # Campo que se define como identificador único (en Odoo la PK es "id" pero se añade este campo para cumplir el enunciado)
    id_autor = fields.Integer(string="ID Autor", required=True, help="Identificador único del autor")
    apellidos = fields.Char(string="Apellidos", required=True)
    nombre = fields.Char(string="Nombre", required=True)

    # Relación One2many con el modelo 'libro'
    libros_publicados = fields.One2many('dcp_library.libro', 'autor_id', string="Libros publicados")

    _sql_constraints = [('id_autor_unique', 'unique(id_autor)', 'El ID del autor debe ser único.')]



class prestamo(models.Model):
    _name = 'dcp_library.prestamo'
    _description = 'Préstamo de libros'

    # Campo identificador único del préstamo
    id_prestamo = fields.Integer(string="ID Préstamo", required=True, help="Identificador único del préstamo")
    # Relación Many2one con el libro que se presta
    libro_prestado_id = fields.Many2one('dcp_library.libro', string="Libro prestado", required=True, ondelete="cascade")
    # Relación Many2one con el cliente que solicita el préstamo
    cliente_id = fields.Many2one('dcp_library.cliente', string="Cliente", required=True, ondelete="cascade")
    fecha_prestamo = fields.Date(string="Fecha de préstamo", required=True)
    fecha_devolucion = fields.Date(string="Fecha de devolución")

    _sql_constraints = [('id_prestamo_unique', 'unique(id_prestamo)', 'El ID del préstamo debe ser único.')]



class cliente(models.Model):
    _name = 'dcp_library.cliente'
    _description = 'Cliente de la biblioteca'

    numero_carnet_biblioteca = fields.Char(string="Número de carné", required=True, help="Identificador único del cliente")
    nombre_completo = fields.Char(string="Nombre completo", required=True)
    fecha_registro = fields.Date(string="Fecha de registro", required=True)
    fecha_caducacion_carnet = fields.Date(string="Fecha de caducidad del carné", required=True)

    # Relación One2many con el modelo 'prestamo'
    prestamos_activos = fields.One2many('dcp_library.prestamo', 'cliente_id', string="Préstamos activos")

    # Relación Many2many con el modelo 'libro' para gestionar los favoritos.
    # Se utiliza la tabla intermedia 'cliente_favoritos'
    favoritos = fields.Many2many('dcp_library.libro', 'cliente_favoritos', 'cliente_id', 'libro_id', string="Favoritos")

    _sql_constraints = [('numero_carnet_unique', 'unique(numero_carnet_biblioteca)', 'El número de carné debe ser único.')]
