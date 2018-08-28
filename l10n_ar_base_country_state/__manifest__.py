# -*- coding: utf-8 -*-
##############################################################################
#
#    Module for Odoo/OpenERP that adds Argentina's States (aka Provinces)
#    Copyright (C) Gabriel Davini. (<https://github.com/gabrielo77>).
#
#    This is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Base Argentina's States (aka Provinces)",
    "version": "11.0.1.0.0",
    "depends": [
        "account",
        "sale",
    ],
    "author": "Gabriel Davini",
    "category": "Base Modules",
    "description": """
    This module provides:
        * States (aka provinces) for Argentina.
    """,
    'data': [
        'data/country_state_data.xml',
        'views/partner_view.xml',
        'views/res_city_view.xml',
        'wizard/wizard_install_argentinean_cities_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}