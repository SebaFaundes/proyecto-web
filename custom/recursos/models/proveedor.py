# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CategoriaRecurso(models.Model):
     _name = 'recursos.categoria'

     name = fields.Char(string="Nombre", required=True)