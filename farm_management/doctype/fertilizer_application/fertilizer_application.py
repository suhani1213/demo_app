from frappe.model.document import Document

class FertilizerApplication(Document):
    def validate(self):
        frappe.msgprint("Validating Fertilizer Application")

