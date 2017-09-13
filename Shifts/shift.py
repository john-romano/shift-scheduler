"""
File: shifts.py
Author: John Romano
----------------------
Base class for shifts
"""

from Employees import employee

class Shift:

    def __init__(self, hours, need):
        self.num_hours = hours  # how long does this shift last?
        self.employee_need = need  # how many employees does this shift need?
        self.assigned_employees = []  # who is assigned to this shift?

    # getters

    def get_duration(self):
        return self.num_hours

    def get_employee_need(self):
        return self.employee_need

    def get_remaining_need(self):
        return self.employee_need - len(self.assigned_employees)

    def get_assigned_employees(self):
        return self.assigned_employees

    # setters
    # NOTE: to avoid circular reference with classes (shift importing employee and emp importing shift, leave setters to
    # inherited classes?
    # UPDATE: doesn't seem to be complaining for now
    def add_employee(self, new_employee):
        assert isinstance(new_employee, employee)
        if len(self.assigned_employees) < self.employee_need:
            self.assigned_employees.append(new_employee)
        else:
            print("This shift is full!")