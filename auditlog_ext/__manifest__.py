# Copyright 2019
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': "Audit Log Extension",
    'version': "13.0",
    'author': "Syncoria",
    'license': "AGPL-3",
    'website': "https://www.syncoria.com/",
    'category': "Tools",
    'depends': [
        'base','auditlog'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/nviews.xml',
        'views/iviews.xml',
        'views/menus.xml'
    ],
    'application': False,
    'installable': True,
}
