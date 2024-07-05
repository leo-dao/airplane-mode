import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe import _

class AirplaneFlight(WebsiteGenerator):
    def validate(self):
        if self.status not in ["Scheduled", "Completed", "Cancelled"]:
            frappe.throw(_("Invalid status"))

    def on_submit(self):
        self.status = 'Completed'

    def get_context(self, context):
        context.published = self.published
        if not self.published:
            raise frappe.PageNotFoundError