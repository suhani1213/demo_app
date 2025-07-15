from frappe.model.document import Document

class FertilizerSuggestion(Document):
    def validate(self):
        frappe.msgprint("Validating Fertilizer Suggestion")
