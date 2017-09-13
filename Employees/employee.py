"""
File: employee.py
Author: John Romano
------------------------
Base class for employees
"""

from Shifts import shift

class Employee:

    employee_count = 0

    def __init__(self, name, availability, priority):
        self.name = name  # what is their name?
        self.availability = availability  # when are they available? (shift objects)
        # need to convert csv data into shift objects before assigning to employees
        self.priority = priority  # what is their priority? (1-10 integer scale)
        self.assigned_shifts = []  # what shifts are they assigned to?
        Employee.employee_count += 1

    # getters

    def get_employee_count(self):
        return Employee.employee_count

    def get_name(self):
        return self.name

    def get_availability(self):
        return self.availability

    def get_priority(self):
        return self.priority

    # setters

    def assign_shift(self, new_shift): # assert type?
        assert isinstance(new_shift, shift)
        self.assigned_shifts.append(new_shift)