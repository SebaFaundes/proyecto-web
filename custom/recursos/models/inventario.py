# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Inventario(models.Model):
     _name = 'recursos.inventario'

     name = fields.Char(string="Nombre", required=True)
     description = fields.Text(string="Descripción")
     supplier = fields.Char(string="Proveedor")