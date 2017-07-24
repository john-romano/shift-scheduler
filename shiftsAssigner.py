#!/usr/bin/env python3 -tt
"""
File: shiftAssigner.py
----------------------
Course: CS 41
Name: John Romano
SUNet: jromano, raythai
"""

import csv 
import collections

NAME_INDEX = 1
NUM_WEEKS = 6
# NOTE: shift days has to change between morning and afternoon shifts!!
SHIFT_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
FILE_NAME = 'july17_morning.csv'

# constructs a mapping from all employees (string) to the shifts that they can work (list)
# weeks in the list are at successive indices, and within each week, days are separated by semicolon
def constructShiftMap(csv):
    unorderedMap = {}
    for employee in csv:
        employeeShifts = employee[0].split('\t')
        name = employeeShifts[NAME_INDEX]
        shifts = employeeShifts[2:]
        unorderedMap[name] = shifts
    return unorderedMap

# constructs a mapping from each day of the month to all people who can work that day
def constructDateMap(shiftMap):
    dateMap = {}
    for day in SHIFT_DAYS:  # TODO: first order of business is finding a better way to make this a list comprehension
        for week_index in range(0, NUM_WEEKS): #NOTE: week 0 is the thursday friday week
            for name, availability in shiftMap.items():
                if day in availability[week_index]:
                    weekDay = "Week " + str(week_index + 1) + " " + day
                    if weekDay in dateMap.keys():
                        dateMap[weekDay].append(name)
                    else:
                        dateMap[weekDay] = [name]
    return dateMap
    
def createdictOfHoursScheduled(shiftMap):
    allWorkers = shiftMap.keys()
    hoursScheduledForPeople = dict()
    for worker in allWorkers:
       hoursScheduledForPeople[worker] = 0
    return hoursScheduledForPeople

    
def findPersonWithLeastHours(peopleWhoCanWork, hoursScheduledForPeople):
    leastAllocatedHours = 1000
    personWithLeastHours = ""
        #finds person with leastAllocatedHours to work
    for person in peopleWhoCanWork:
        hoursForPerson = hoursScheduledForPeople.get(person)
        if hoursForPerson < leastAllocatedHours:
            leastAllocatedHours = hoursForPerson
            personWithLeastHours = person
    return personWithLeastHours


"""
unCoveredShifts is a dictionary of shifts to people who can work those shifts
allWorkers is a list of all possible workers
"""
def createCalendar(unCoveredShifts, hoursScheduledForPeople):
    calendar = dict()
    for shift, peopleWhoCanWork in unCoveredShifts.items():
        i = 0
        while i <= 5 and peopleWhoCanWork:
            personWithLeastHours = findPersonWithLeastHours(peopleWhoCanWork, hoursScheduledForPeople)
            if shift in calendar.keys():
                calendar[shift].append(personWithLeastHours)
            else:
                calendar[shift] = [personWithLeastHours]
            hoursScheduledForPeople[personWithLeastHours] += 1
            unCoveredShifts[shift].remove(personWithLeastHours)
            i += 1
    return calendar
    
if __name__ == '__main__':
    with open(FILE_NAME) as f:
        availability = csv.reader(f)
        shiftMap = constructShiftMap(availability)
        dateMap = constructDateMap(shiftMap)
        hoursScheduledForPeople = createdictOfHoursScheduled(shiftMap)
        calendar = createCalendar(dateMap, hoursScheduledForPeople)
        list = sorted(calendar.keys())
        for shift in list:
            print(shift, ':',end = " ")
            for person in calendar[shift]:
                print(person, end =" ")
            print()
        # pass in shift map or availability?
        #priorityMap = constructPriorityMap(availability)
        # init map of employees to num hours worked for each; probably don't need separate method   
    # 3) assign employees to shifts to create mapping of employees to assigned shifts (map of dates to people)