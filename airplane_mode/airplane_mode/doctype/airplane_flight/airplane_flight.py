# Copyright (c) 2024, Leo Dao and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(Document):
	def on_submit(self):
		self.status = 'Completed'