from frappe.model.document import Document

class PlantationMaster(Document):
    def validate(self):
        frappe.msgprint("Validating Plantation Master")
