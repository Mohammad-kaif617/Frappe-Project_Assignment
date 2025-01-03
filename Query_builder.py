import frappe

def fetch_in_progress_tasks():
    current_user = frappe.session.user
    tasks = (
        frappe.qb.from_("`tabProject Task`")
        .select("name", "task_name", "status", "assigned_to")
        .where(
            (frappe.qb.Field("status") == "In Progress")
            & (frappe.qb.Field("assigned_to") == current_user)
        )
    ).run()
    return tasks
