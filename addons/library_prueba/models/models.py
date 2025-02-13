# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class libro(models.Model):
    _name = 'library_prueba.libro'
    _description = 'Libro de la biblioteca'
    _order = 'titulo'
    _rec_name = 'titulo'  # He añadido esto porque me esta estaba dando errores. Representa el nombre de los registros del modelo.

    isbn = fields.Char(string="ISBN", required=True, help="Identificador único del libro")
    titulo = fields.Char(string="Título", required=True)
    autor_id = fields.Many2one('library_prueba.autor', string="Autor", required=True, ondelete="cascade")
    fecha_publicacion = fields.Date(string="Fecha de publicación", required=True)
    editorial = fields.Char(string="Editorial")
    edicion = fields.Char(string="Edición")
    numero_categoria = fields.Integer(string="Número de categoría", help="Número que indica la categoría según el Sistema Dewey")
    valor = fields.Float(string="Valor económico")
    en_biblioteca = fields.Boolean(string="En biblioteca", default=True)
    estado = fields.Selection(selection=[('nuevo', 'Nuevo'), ('usado', 'Usado'), ('deteriorado', 'Deteriorado')], string="Estado", required=True)
    # Relación con el modelo 'prestamo'
    prestamos_ids = fields.One2many('library_prueba.prestamo', 'libro_prestado_id', string="Préstamos")
    # Relación Many2many con clientes (favoritos)
    cliente_ids = fields.Many2many('library_prueba.cliente', 'cliente_favoritos', 'libro_id', 'cliente_id', string="Clientes que marcaron este libro como favorito")
    # Campo de imagen de la portada (tipo Binary)
    portada = fields.Binary(string="Portada", attachment=True, help="Imagen de la portada del libro")
    # Campo calculado que cuenta el número de préstamos
    prestamos_count = fields.Integer(string="Número de Préstamos", compute="_compute_prestamos_count", store=True, help="Número de veces que este libro ha sido prestado")

    @api.depends("prestamos_ids")
    def _compute_prestamos_count(self):
        for record in self:
            record.prestamos_count = len(record.prestamos_ids)


class autor(models.Model):
    _name = 'library_prueba.autor'
    _description = 'Autor de libros'
    _order = 'apellidos, nombre'
    _rec_name = 'nombre'

    # Campo que se define como identificador único (en Odoo la PK es "id" pero se añade este campo para cumplir el enunciado)
    id_autor = fields.Integer(string="ID Autor", required=True, help="Identificador único del autor")
    apellidos = fields.Char(string="Apellidos", required=True)
    nombre = fields.Char(string="Nombre", required=True)

    # Relación One2many con el modelo 'libro'
    libros_publicados = fields.One2many('library_prueba.libro', 'autor_id', string="Libros publicados")


class prestamo(models.Model):
    _name = 'library_prueba.prestamo'
    _description = 'Préstamo de libros'
    _order = 'fecha_prestamo desc'

    # Campo identificador único del préstamo
    id_prestamo = fields.Integer(string="ID Préstamo", required=True, help="Identificador único del préstamo")
    # Relación Many2one con el libro que se presta
    libro_prestado_id = fields.Many2one('library_prueba.libro', string="Libro prestado", required=True, ondelete="cascade")
    # Relación Many2one con el cliente que solicita el préstamo
    cliente_id = fields.Many2one('library_prueba.cliente', string="Cliente", required=True, ondelete="cascade")
    fecha_prestamo = fields.Date(string="Fecha de préstamo", required=True)
    fecha_devolucion = fields.Date(string="Fecha de devolución")

    @api.constrains('fecha_prestamo', 'fecha_devolucion')
    def _check_fechas(self):
        for record in self:
            if record.fecha_devolucion and record.fecha_prestamo > record.fecha_devolucion:
                raise ValidationError('La fecha de devolución debe ser posterior a la fecha de préstamo')


class cliente(models.Model):
    _name = 'library_prueba.cliente'
    _description = 'Cliente de la biblioteca'
    _order = 'fecha_registro desc'
    _rec_name = 'nombre_completo'

    numero_carnet_biblioteca = fields.Char(string="Número de carné", required=True, help="Identificador único del cliente")
    nombre_completo = fields.Char(string="Nombre completo", required=True)
    fecha_registro = fields.Date(string="Fecha de registro", required=True)
    fecha_caducacion_carnet = fields.Date(string="Fecha de caducidad del carné", required=True)

    # Relación One2many con el modelo 'prestamo'
    prestamos_activos = fields.One2many('library_prueba.prestamo', 'cliente_id', string="Préstamos activos")

    # Relación Many2many con el modelo 'libro' para gestionar los favoritos.
    # Se utiliza la tabla intermedia 'cliente_favoritos'
    favoritos = fields.Many2many('library_prueba.libro', 'cliente_favoritos', 'cliente_id', 'libro_id', string="Favoritos")
