# Copyright (c) 2024, Leo Dao and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns, data = [], []

    columns = [
        {"fieldname": "airport", "label": _("Airport"), "fieldtype": "Link", "options": "Airport", "width": 150},
        {"fieldname": "total_shops", "label": _("Total Shops"), "fieldtype": "Int", "width": 100},
        {"fieldname": "available_shops", "label": _("Available Shops"), "fieldtype": "Int", "width": 100},
        {"fieldname": "occupied_shops", "label": _("Occupied Shops"), "fieldtype": "Int", "width": 100}
    ]

    airports = frappe.get_all("Airport", fields=["name"])

    for airport in airports:
        total_shops = frappe.db.count("Shop", {"airport": airport.name})
        available_shops = frappe.db.count("Shop", {"airport": airport.name, "status": "Available"})
        occupied_shops = frappe.db.count("Shop", {"airport": airport.name, "status": "Occupied"})

        data.append({
            "airport": airport.name,
            "total_shops": total_shops,
            "available_shops": available_shops,
            "occupied_shops": occupied_shops
        })

    return columns, data
