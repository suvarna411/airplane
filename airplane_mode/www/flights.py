import frappe

def get_context(context):
    context.docs = frappe.get_all(
        "Airplane Flight",
        filters={"is_published": 1},
        fields=[
            "name",
            "source_airport",
            "destination_airport",
            "date_of_departure",
            "time_of_departure",
            "duration",
            "route"
        ]
    )
