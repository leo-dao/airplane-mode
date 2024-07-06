# Copyright (c) 2024, Leo Dao and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
import random
import string

class AirplaneTicket(Document):
    
	def before_submit(self):
		if self.status != 'Boarded':
			frappe.throw(_("This ticket cannot be submitted because the status is not 'Boarded'."))

	def validate_capacity(self):

		# Get the airplane linked to the flight
		flight_doc = frappe.get_doc("Airplane Flight", self.flight)
		
		airplane_doc = frappe.get_doc("Airplane", flight_doc.airplane)

		existing_tickets = frappe.get_all(
            "Airplane Ticket",
            filters={"flight": self.flight},
            fields=["name", "passenger"]
        )

		# Check if the passenger already has a ticket for the flight
		num_unique_tickets = len(existing_tickets)

		for ticket in existing_tickets:
			if ticket['name'] == self.name:
				num_unique_tickets -= 1
			
		# Compare with airplane capacity
		if num_unique_tickets >= airplane_doc.capacity:
			frappe.throw(_("Cannot create more tickets. Airplane capacity exceeded."))


	def validate(self):

		self.validate_capacity()

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
		
		# Convert flight_price to float for calculation
		if isinstance(self.flight_price, str):
			try:
				self.flight_price = float(self.flight_price.replace(',', '.'))
			except ValueError:
				frappe.throw(_("Invalid flight price format. Please enter a valid number."))
		elif not isinstance(self.flight_price, (int, float)):
			frappe.throw(_("Flight price must be a number."))
		
		self.total_amount = self.flight_price + addons_sum