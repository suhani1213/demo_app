from frappe.model.document import Document

class FertilizerPlan(Document):
    def validate(self):
        frappe.msgprint("Validating Fertilizer Plan")
