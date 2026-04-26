# Copyright (c) 2026, suvarna and contributors
# For license information, please see license.txt

import random
import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):

   
    def before_insert(self):
        number = random.randint(1, 100)
        letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        self.seat = f"{number}{letter}"

   
    def validate(self):
        self.remove_duplicate_addons()
        self.calculate_total()
        if self.flight:
            airplane = frappe.db.get_value("Flight", self.flight, "airplane")
            capacity = frappe.db.get_value("Airplane", airplane, "capacity")

            count = frappe.db.count("Airplane Ticket", {
               "flight": self.flight,
               "docstatus": 1
              })

            if count >= capacity:
                frappe.throw("Flight is fully booked!")

   
    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("Cannot submit ticket unless status is Boarded")

   
    def calculate_total(self):
        total_addons = sum(d.amount for d in self.add_ons)
        self.total_amount = self.flight_price + total_addons

    def remove_duplicate_addons(self):
        unique = []
        seen = set()

        for d in self.add_ons:
            if d.item not in seen:
                seen.add(d.item)
                unique.append(d)

        self.add_ons = unique
