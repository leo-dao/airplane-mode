import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe import _

class AirplaneFlight(WebsiteGenerator):

    def on_submit(self):
        self.status = 'Completed'