frappe.listview_settings['Project Task'] = {
    get_indicator: function (doc) {
        if (doc.end_date && frappe.datetime.get_diff(doc.end_date) < 0) {
            return ['Overdue', 'red', 'end_date,<,Today'];
        }
    }
};
