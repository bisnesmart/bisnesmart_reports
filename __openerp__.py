# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Informes BisneSmart",
    "version": "1.0",
    "author": "BisneSmart Team,"
              "BisneSmart",
    "contributors": [
        "Gonzalo Borras <gborras@bisnesmart.com>",
        "Ruben Cabrera <rcabrera@bisnesmart.com>",
        "Departamento Odoo <odoo@bisnesmart.com>",
    ],
    "website": "http://www.bisnesmart.com",
    "depends": [
        "account",
        "product",
        "base",
        "sale",
    ],
    "data": [
        "views/sale/report_saleorder_bisnesmart.xml",
        "views/sale/report_saleorder_bisnesmart_document.xml",
        "views/external_layout/external_layout_header_bisnesmart.xml",
        "views/external_layout/external_layout_footer_bisnesmart.xml",

    ],    
    "installable": True,
    "application": True,
    "active": True,
}
