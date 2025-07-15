from frappe.model.document import Document

class FertilizerCalculation(Document):
    def validate(self):
        frappe.msgprint("Validating Fertilizer Calculation")
