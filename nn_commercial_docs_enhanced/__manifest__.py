# -*- coding: utf-8 -*-
{
    'name': 'Personnalisation des Documents (Factures, Devis, BC, BL, Stock)',
    'version': '1.0.0',
    'category': 'Personnalisation',
    'summary': 'Améliorations des documents : factures, devis, bons de commande, livraison, stock et achats',
    'description': """
Ce module regroupe plusieurs personnalisations pour les documents Odoo :

- Factures : logo optionnel, suppression du timbre fiscal, affichage du montant en lettres, signature numérique, etc.
- Devis : gestion multidevise, champs personnalisés, modèle PDF unifié.
- Bons de commande : suppression de la date de demande, signature numérique, simplification des montants.
- Bons de livraison : ajout de PN, SN, modèle PDF cohérent.
- Achats : informations supplémentaires et personnalisation du PDF.
- Stock : filtres avancés, champs supplémentaires, affichage simplifié des montants.
- Ajout d’un module de gestion des tickets.
- Signature numérique sur tous les documents.
""",
    'author': 'Ouchari Ibrahim / NeoNara',
    'depends': [
        'base',
        'account',
        'sale',
        'purchase',
        'stock',
        'mail',  # pour les envois d’e-mail avec signature
        'web',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move_views.xml',
        'reports/account_invoice_report_template.xml',

    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
