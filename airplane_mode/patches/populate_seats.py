import frappe
import random

def execute():
    tickets = frappe.get_all("Airplane Ticket", fields=["name"])

    for t in tickets:
        doc = frappe.get_doc("Airplane Ticket", t.name)

        if not doc.seat:
            number = random.randint(1, 100)
            letter = random.choice(['A','B','C','D','E'])
            doc.seat = f"{number}{letter}"
            doc.db_update()
