# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryBook(models.Model):
    _inherit = "library.book"

    author_id = fields.Many2one(
        comodel_name='res.partner', string='Author'
    )
    category_ids = fields.Many2many(
        comodel_name="library.book.category",
        string="Categories",
    )