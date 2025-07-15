from frappe.model.document import Document

class FarmMaster(Document):
    def validate(self):
        frappe.msgprint("Validating Farm Master")
