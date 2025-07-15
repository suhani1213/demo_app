import frappe

@frappe.whitelist()
def generate_fertilizer_plan(plantation_name):
    # TODO: implement logic here
    return f"Fertilizer plan generated for {plantation_name}"
