# Copyright (c) 2024, Leo Dao and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Airport(Document):
	
	def update_shop_count(airport_name):
		shop_count = frappe.db.count('Shop', filters={'airport': airport_name})
		frappe.db.set_value('Airport', airport_name, 'shop_count', shop_count)
		frappe.db.commit()
