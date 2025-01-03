frappe.ui.form.on('Project Task', {
    refresh: function (frm) {
        frm.add_custom_button('Mark as Completed', () => {
            frm.set_value('status', 'Completed');
            frappe.msgprint(__('Task marked as Completed!'));
        });
    }
});
