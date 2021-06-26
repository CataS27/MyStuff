"""
A factory needs an iterable object to keep track of employee working schedule for each day.
Each employee has a string name and an object of type datetime that indicate when employee started work
Iterating the object will return tuple with name and time that employee entered the factory
1) 40p: Definition
    a) 10p: Class with constructor that receives the date in the format you desire (representing the day)
    b) 10p: Create method to add worker information when he/she enters the factory
         - if worker is already in the factory a custom exception inheriting ValueError (exception: WorkStartError)
         will be raised with message indicating employee name and current time
    c) 10p: Create method to remove worker information when he/she leaves the factory
         - if worker is not in the factory a custom exception inheriting ValueError (exception: WorkEndError)
         will be raised with message indicating employee name and current time
    c) 10p: Iterating the object will return tuple with name and time employee entered the factory
2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add the following employees with time of arrival:
        - Joe: 09:01:20
        - Ana: 09:03:15
        - Tim: 09:04:25
        - Tim: 09:04:30 - treat this exception
    c) 10p: Remove teh following employees:
        - Joe
        - Ana
        - Tim
        - Tim - treat this exception
    d) 10p: Iterate the created object and save each value on a new line in a file
3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""

from datetime import datetime


class Start(ValueError):
    pass


class End(ValueError):
    pass


class TimeIter:
    """Iterator for starting hours by name"""

    def __init__(self, start_time: list):
        self.start_time = start_time

    def __iter__(self):
        return self

    def __next__(self):
        if not self.start_time:
            raise StopIteration
        else:
            return self.start_time.pop(0)


class TimeKeeper:
    """keeps track of entering hours for employees"""
    ledger = {}

    def __init__(self, date: list):
        self.date = date

    def __iter__(self):
        result = []
        for name, entry_time in self.ledger.items():
            result.append((name, entry_time))
        return TimeIter(result)

    def entry_time(self, name: str, entry_time: list):
        """add worker"""
        if self.ledger.get(name, None):
            raise Start(f'{name} already started work')
        self.ledger[name] = datetime(*self.date, *entry_time)

    def remove_worker(self, name: str):
        """remove worker"""
        if self.ledger.get(name) is None:
            raise End(f'{name} not present {datetime.now()}')
        self.ledger.pop(name)


timer = TimeKeeper([2021, 5, 8])

# add start time
timer.entry_time('Joe', [9, 1, 20])
timer.entry_time('Ana', [9, 3, 15])
timer.entry_time('Tim', [9, 4, 25])
try:
    timer.entry_time('Tim', [9, 4, 30])
except Start as s:
    print(s)

# remove from the factory
timer.remove_worker('Joe')
timer.remove_worker('Ana')
timer.remove_worker('Tim')
try:
    timer.remove_worker('Tim')
except End as s:
    print(s)
