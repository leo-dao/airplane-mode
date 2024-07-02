# Copyright (c) 2024, Leo Dao and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string

class AirplaneTicket(Document):
    
	def before_submit(self):
		if self.status != 'Boarded':
			frappe.throw(_("This ticket cannot be submitted because the status is not 'Boarded'."))

	def before_insert(self):
		random_integer = random.randint(1, 100)
		random_letter = random.choice('ABCDE')
		self.seat = f"{random_integer}{random_letter}"

	def validate(self):
		addons_sum = 0
		unique_addons = set()
		duplicates = []
		for index, addon in enumerate(self.add_ons):
			if addon.add_on_type in unique_addons:
				duplicates.append(index)
			else:
				addons_sum += addon.amount
				unique_addons.add(addon.add_on_type)
		
		for index in duplicates:
			self.remove(self.add_ons[index])
		
		self.total_amount = self.flight_price + addons_sum