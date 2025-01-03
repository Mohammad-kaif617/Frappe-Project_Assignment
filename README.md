none
# Frappe Project Management App

This repository contains a Frappe-based application for managing projects and tasks.

## Features
1. Custom Doctype: `Project Task`
   - Fields: Task Name, Project, Start Date, End Date, Assigned To, Status
   - Validation: Ensures End Date is not before Start Date.

2. Client Script:
   - Automatically updates task status based on Start Date and End Date.
   - Custom button to mark a task as completed.

3. ListView Customization:
   - Highlights overdue tasks in red.

4. API Endpoint:
   - Fetches tasks assigned to a specific user.

5. Workflow:
   - `Not Started → In Progress → Completed`
   - Only the task assignee can move tasks to "Completed".
