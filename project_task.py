from frappe.model.document import Document
from frappe import _

class ProjectTask(Document):
    def validate(self):
        if self.end_date and self.start_date and self.end_date < self.start_date:
            frappe.throw(_("End Date cannot be before Start Date"))
