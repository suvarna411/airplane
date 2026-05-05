# Copyright (c) 2026, suvarna and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):

    def on_update(self):
        frappe.logger().info("ON UPDATE TRIGGERED")
        if self.has_value_changed("gate_number"):

            frappe.logger().info("GATE CHANGED")
            frappe.enqueue(
                "airplane_mode.airplane_mode.doctype.airplane_flight.airplane_flight.update_ticket_gate",
                flight=self.name
            )


def update_ticket_gate(flight):
    tickets = frappe.get_all("Ticket", filters={"flight": flight})
    
    gate = frappe.db.get_value("Airplane Flight", flight, "gate_number")

    for t in tickets:
        doc = frappe.get_doc("Ticket", t.name)
        doc.gate_number = gate
        doc.save(ignore_permissions=True)
