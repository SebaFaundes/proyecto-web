# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CategoriaRecurso(models.Model):
     _name = 'recursos.categoria'

     name = fields.Char(string="Nombre", required=True)

class Inventario(models.Model):
     _name = 'recursos.inventario'

     name = fields.Char(string="Nombre", required=True)
     description = fields.Text(string="Descripción")
     supplier = fields.Char(string="Proveedor")

     categoria_id = fields.Many2one('recursos.categoria', string="Categoría de Producto")