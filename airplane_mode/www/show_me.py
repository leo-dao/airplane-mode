import frappe
from frappe import _

def get_context(context):
    # Get the color from the query parameter, default to 'black' if not provided
    color = frappe.form_dict.color if 'color' in frappe.form_dict else 'black'
    
    context.color = color
    context.title = _("Show Me")