# Copyright (c) 2026, suvarna and contributors
# For license information, please see license.txt

# import frappe
import frappe

def execute(filters=None):
    columns = [
        {
            "label": "Airline",
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width": 200
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 150
        }
    ]

    data = []
    total_revenue = 0

    airlines = frappe.get_all("Airline", fields=["name"])

    tickets = frappe.get_all(
        "Airplane Ticket",
        filters={"docstatus": 1},
        fields=["flight", "total_amount"]
    )

    for airline in airlines:
        revenue = 0

        for t in tickets:
            airplane = frappe.db.get_value(
                "Airplane Flight", t.flight, "airplane"
            )

            airline_name = frappe.db.get_value(
                "Airplane", airplane, "airline"
            )

            if airline_name == airline.name:
                revenue += float(t.total_amount or 0)

        total_revenue += revenue

        data.append({
            "airline": airline.name,
            "revenue": revenue
        })

    chart = {
        "data": {
            "labels": [d["airline"] for d in data],
            "datasets": [
                {
                    "name": "Revenue",
                    "values": [d["revenue"] for d in data]
                }
            ]
        },
        "type": "donut"
    }

    
    summary = [
        {
            "label": "Total Revenue",
            "value": total_revenue,
            "indicator": "Green"
        }
    ]

    return columns, data, None, chart, summary
